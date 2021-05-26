# distutils: language = c++

STR_ROTORS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    "ESOVPZJAYQUIRHXLNFTGKDCMWB",
    "VZBRGITYUPSDNHLXAWMJQOFECK",
    ]
ROTOR_NOTCHES = [ord(c) - 65 for c in "QEVJZ"]
STR_REFLECTORS = [
    "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    ]

ROTORS = [[ord(c) - 65 for c in rotor] for rotor in STR_ROTORS]
INV_ROTORS = [[0] * 26 for _ in range(len(STR_ROTORS))]
for i, r in enumerate(ROTORS):
    for x, y in enumerate(r):
        INV_ROTORS[i][y] = x

REFLECTORS = [[ord(c) - 65 for c in reflector] for reflector in STR_REFLECTORS]

class Enigma:
    def __init__(self, reflector, rotors, position, rings, plugboard):
        self.num_rotors = len(rotors)
        self.rotors = rotors
        self.reflector = reflector
        self.notches = [ROTOR_NOTCHES[rotor] for rotor in self.rotors]

        mapping = list(range(26))
        for k, v in zip(plugboard[::3], plugboard[1::3]):
            mapping[ord(k) - 65] = ord(v) - 65
            mapping[ord(v) - 65] = ord(k) - 65
        self.plugboard = mapping

        self.offsets = position
        self.rings = rings

    def score(self, word):
        freq = [0] * 26
        for letter in self(word):
            freq[ord(letter) - 65] += 1

        freq[c] += 1

        return sum(x*x for x in freq)

    def __call__(self, word):
        offsets = list(self.offsets)  # Work with a local copy.
        output = []
        for letter in word:
            # Rotate the offsets.
            for i in range(self.num_rotors):
                if offsets[i] == ROTOR_NOTCHES[self.rotors[i]]:
                    if i < self.num_rotors - 1:
                        offsets[i] = (offsets[i] + 1) % 26
                    if i > 0:
                        offsets[i-1] = (offsets[i-1] + 1) % 26
            offsets[self.num_rotors-1] = (offsets[self.num_rotors-1] + 1) % 26

            c = ord(letter) - 65

            c = self.plugboard[c]

            for rotor, offset, ring in zip(reversed(self.rotors), reversed(offsets), reversed(self.rings)):
                shift = offset - ring
                c = (ROTORS[rotor][(c + shift) % 26] - shift) % 26

            c = REFLECTORS[self.reflector][c]

            for rotor, offset, ring in zip(self.rotors, offsets, self.rings):
                shift = offset - ring
                c = (INV_ROTORS[rotor][(c + shift) % 26] - shift) % 26

            c = self.plugboard[c]

            output.append(c)

        return ''.join(chr(x + 65) for x in output)

