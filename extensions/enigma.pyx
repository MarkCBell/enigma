# distutils: language = c++

from cpython cimport array
import array

cimport enigma

STR_ROTORS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    "ESOVPZJAYQUIRHXLNFTGKDCMWB",
    "VZBRGITYUPSDNHLXAWMJQOFECK",
    ]
cdef array.array ROTOR_NOTCHES = array.array('i', [ord(c) - 65 for c in "QEVJZ"])

STR_REFLECTORS = [
    "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    ]

cdef array.array FREQ = array.array('i', [0] * 26)
cdef array.array ROTORS = array.array('i', [ord(c) - 65 for rotor in STR_ROTORS for c in rotor])
cdef array.array INV_ROTORS = array.array('i', [0] * 26 * len(STR_ROTORS))
for i, r in enumerate(STR_ROTORS):
    for x, y in enumerate(r):
        INV_ROTORS[26 * i + ord(y) - 65] = x
cdef array.array REFLECTORS = array.array('i', [ord(c) - 65 for reflector in STR_REFLECTORS for c in reflector])

cdef class Enigma:
    def __init__(self, reflector, rotors, position, rings, plugboard):
        cdef int i

        self.num_rotors = len(rotors)
        self.rotors = array.array('i', rotors)
        self.reflector = reflector

        mapping = list(range(26))
        for k, v in zip(plugboard[::3], plugboard[1::3]):
            mapping[ord(k) - 65] = ord(v) - 65
            mapping[ord(v) - 65] = ord(k) - 65
        self.plugboard = array.array('i', mapping)

        self.offsets = array.array('i', position)
        self.rings = array.array('i', rings)

    def score(self, str word):
        cdef int i, j, length
        cdef int c, s, w, x, y
        cdef array.array offsets, sequence, freq

        length = len(word)
        sequence = array.array('i', [ord(letter) - 65 for letter in word])
        offsets = array.copy(self.offsets)  # Work with a local copy.
        freq = array.clone(FREQ, 26, True)
        for j in range(length):
            # Rotate the offsets.
            for i in range(self.num_rotors):
                if offsets.data.as_ints[i] == ROTOR_NOTCHES.data.as_ints[self.rotors.data.as_ints[i]]:
                    if i < self.num_rotors - 1:
                        offsets.data.as_ints[i] = (offsets.data.as_ints[i] + 1) % 26
                    if i > 0:
                        offsets.data.as_ints[i-1] = (offsets.data.as_ints[i-1] + 1) % 26
            offsets.data.as_ints[self.num_rotors-1] = (offsets.data.as_ints[self.num_rotors-1] + 1) % 26

            c = sequence.data.as_ints[j]

            c = self.plugboard.data.as_ints[c]
            for i in range(self.num_rotors-1, -1, -1):
                w = self.rotors.data.as_ints[i]
                x = offsets.data.as_ints[i]
                y = self.rings.data.as_ints[i]
                c = (ROTORS.data.as_ints[26 * w + ((c + x - y) % 26)] - x + y) % 26

            c = REFLECTORS.data.as_ints[26 * self.reflector + c]

            for i in range(self.num_rotors):
                w = self.rotors.data.as_ints[i]
                x = offsets.data.as_ints[i]
                y = self.rings.data.as_ints[i]
                c = (INV_ROTORS.data.as_ints[26 * w + ((c + x - y) % 26)] - x + y) % 26

            c = self.plugboard.data.as_ints[c]

            freq.data.as_ints[c] += 1

        s = 0
        for i in range(26):
            s += freq.data.as_ints[i] * freq.data.as_ints[i]
        return s

    def __call__(self, str word):
        cdef int i, j, length
        cdef int c, w, x, y
        cdef array.array offsets, sequence, output

        length = len(word)
        sequence = array.array('i', [ord(letter) - 65 for letter in word])
        offsets = array.copy(self.offsets)  # Work with a local copy.
        output = array.clone(FREQ, length, True)
        for j in range(length):
            # Rotate the offsets.
            for i in range(self.num_rotors):
                if offsets.data.as_ints[i] == ROTOR_NOTCHES.data.as_ints[self.rotors.data.as_ints[i]]:
                    if i < self.num_rotors - 1:
                        offsets.data.as_ints[i] = (offsets.data.as_ints[i] + 1) % 26
                    if i > 0:
                        offsets.data.as_ints[i-1] = (offsets.data.as_ints[i-1] + 1) % 26
            offsets.data.as_ints[self.num_rotors-1] = (offsets.data.as_ints[self.num_rotors-1] + 1) % 26

            c = sequence.data.as_ints[j]

            c = self.plugboard.data.as_ints[c]
            for i in range(self.num_rotors-1, -1, -1):
                w = self.rotors.data.as_ints[i]
                x = offsets.data.as_ints[i]
                y = self.rings.data.as_ints[i]
                c = (ROTORS.data.as_ints[26 * w + ((c + x - y) % 26)] - x + y) % 26

            c = REFLECTORS.data.as_ints[26 * self.reflector + c]

            for i in range(self.num_rotors):
                w = self.rotors.data.as_ints[i]
                x = offsets.data.as_ints[i]
                y = self.rings.data.as_ints[i]
                c = (INV_ROTORS.data.as_ints[26 * w + ((c + x - y) % 26)] - x + y) % 26

            c = self.plugboard.data.as_ints[c]

            output.data.as_ints[j] = c

        return ''.join(chr(x + 65) for x in output)

