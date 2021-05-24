
encode = lambda c: ord(c) - 65
decode = lambda x: chr(x + 65)

class Permutation:
    def __init__(self, forwards, backwards, name=None):
        self.forwards = forwards
        self.backwards = backwards
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)

    def __call__(self, c):
        return self.forwards[c]

    def __getitem__(self, c):
        return self.backwards[c]

    def __invert__(self):
        return Permutation(self.backwards, self.forwards, self.name)

    def is_order2(self):
        return all(self(self(c)) == c for c in range(26))

    @classmethod
    def from_string(cls, strn, name=None):
        if name is None: name = strn
        forwards = [encode(c) for c in strn]
        backwards = [None] * 26
        for i, j in enumerate(forwards):
            backwards[j] = i

        return cls(forwards, backwards, name)

    @classmethod
    def from_shift(cls, k, name=None):
        if name is None: name = str(k)
        forwards = [(i + k) % 26 for i in range(26)]
        backwards = [(i - k) % 26 for i in range(26)]
        return cls(forwards, backwards, name)

    @classmethod
    def from_pairs(cls, strn, name=None):
        if name is None: name = strn
        mapping = list(range(26))
        for k, v in zip(strn[::3], strn[1::3]):
            mapping[encode(k)] = encode(v)
            mapping[encode(v)] = encode(k)
        return cls(mapping, mapping, name)


# Real rotors.
def rotors():
    return (
        Permutation.from_string("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "I"),  # {16},
        Permutation.from_string("AJDKSIRUXBLHWTMCQGZNPYFVOE", "II"),  # {4}
        Permutation.from_string("BDFHJLCPRTXVZNYEIWGAKMUSQO", "III"),  # {21}
        Permutation.from_string("ESOVPZJAYQUIRHXLNFTGKDCMWB", "IV"),  # {9}
        Permutation.from_string("VZBRGITYUPSDNHLXAWMJQOFECK", "V"),  # {25}
        Permutation.from_string("JPGVOUMFYQBENHZRDKASXLICTW", "VI"),  # {12, 25}  # {0, 13}
        Permutation.from_string("NZJHGRCXMYSWBOUFAIVLPEKQDT", "VII"),  # {12, 25}  # {0, 13}
        Permutation.from_string("FKQHTLXOCBJSPDZRAMEWNIUYGV", "VIII"),  # {12, 25}  # {0, 13}
        )

# Real reflectors.
def reflectors():
    return (
        Permutation.from_string("YRUHQSLDPXNGOKMIEBFZCWVJAT", "B"),
        Permutation.from_string("FVPJIAOYEDRZXWGCTKUQSBNMHL", "C"),
        )


class Enigma:
    def __init__(self, reflector, rotors, offsets, rings, plugboard):
        self.reflector = reflector
        self.rotors = rotors
        self.offsets = offsets
        self.rings = rings
        self.plugboard = Permutation.from_pairs(plugboard)
        assert self.reflector.is_order2()
        self.shifts = [Permutation.from_shift(i) for i in range(26)]

    def __call__(self, word):
        sequence = [encode(letter) for letter in word]
        offsets = list(self.offsets)  # Work with a local copy.
        output = []
        for p in sequence:
            # Rotate the offsets.
            # THIS IS NOT CORRECT
            for i in range(len(offsets)):
                offsets[i] = (offsets[i] + 1) % 26
                if offsets[i] != self.rings[i]: break

            # enigma map = reflector**(rotor1**offset1 * rotor2**offset2 * ... * rotorN**offsetN * plugboard)
            c = p

            c = self.plugboard(c)
            for rotor, k in zip(self.rotors, offsets):
                shift = self.shifts[k]
                c = shift[rotor(shift(c))]

            c = self.reflector(c)

            for rotor, k in zip(reversed(self.rotors), reversed(offsets)):
                shift = self.shifts[k]
                c = shift[rotor[shift(c)]]
            c = self.plugboard[c]

            output.append(c)

        return ''.join(decode(x) for x in output)


if __name__ == '__main__':
    I, II, III, IV, V, VI, VII, VIII = rotors()
    B, C = reflectors()
    E = Enigma([I, II, III], B, '', [0, 0, 0], [0, 0, 0])
    p = 'AAAAAAA'
    print(E(p))
    assert p == E(E(p))

