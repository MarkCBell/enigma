
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
        return self.forwards(c)

    def __getitem__(self, c):
        return self.backwards(c)

    def __invert__(self):
        return Permutation(self.backwards, self.forwards, self.name)

    def is_order2(self):
        return all(self(self(c)) == c for c in range(26))

    @classmethod
    def from_string(cls, strn, name=None):
        if name is None: name = strn
        forwards = [ord(c) - 65 for c in strn]
        backwards = [None] * 26
        for i, j in enumerate(forwards):
            backwards[j] = i

        return cls(lambda c: forwards[c], lambda c: backwards[c], name)

    @classmethod
    def from_shift(cls, k, name=None):
        return ROTATIONS[k]

    @classmethod
    def build_from_shift(cls, k, name=None):
        if name is None: name = str(k)
        return cls(lambda c: (c + k) % 26, lambda c: (c - k) % 26, name)

    @classmethod
    def from_pairs(cls, strn, name=None):
        if name is None: name = strn
        mapping = dict()
        for k, v in zip(strn[::3], strn[1::3]):
            mapping[encode(k)] = encode(v)
            mapping[encode(v)] = encode(k)
        return cls(lambda c: mapping.get(c, c), lambda c: mapping.get(c, c), name)


ROTATIONS = [Permutation.build_from_shift(i) for i in range(26)]  # Cache
Id = Permutation.from_shift(0, "Id")

# Real rotors.
I = Permutation.from_string("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "I")  # {16}
II = Permutation.from_string("AJDKSIRUXBLHWTMCQGZNPYFVOE", "II")  # {4}
III = Permutation.from_string("BDFHJLCPRTXVZNYEIWGAKMUSQO", "III")  # {21}
IV = Permutation.from_string("ESOVPZJAYQUIRHXLNFTGKDCMWB", "IV")  # {9}
V = Permutation.from_string("VZBRGITYUPSDNHLXAWMJQOFECK", "V")  # {25}
VI = Permutation.from_string("JPGVOUMFYQBENHZRDKASXLICTW", "VI")  # {12, 25}  # {0, 13}
VII = Permutation.from_string("NZJHGRCXMYSWBOUFAIVLPEKQDT", "VII")  # {12, 25}  # {0, 13}
VIII = Permutation.from_string("FKQHTLXOCBJSPDZRAMEWNIUYGV", "VIII")  # {12, 25}  # {0, 13}

# Real reflectors.
B = Permutation.from_string("YRUHQSLDPXNGOKMIEBFZCWVJAT", "B")
C = Permutation.from_string("FVPJIAOYEDRZXWGCTKUQSBNMHL", "C")
Rev = Permutation.from_string("ZYXWVUTSRQPONMLKJIHGFEDCBA", "Rev")


class Enigma:
    def __init__(self, rotors, reflector, plugboard, restarts, offsets):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = Permutation.from_pairs(plugboard)
        self.restarts = restarts
        self.offsets = offsets
        assert self.reflector.is_order2()

    def __call__(self, word):
        sequence = [encode(letter) for letter in word]
        offsets = list(self.offsets)  # Work with a local copy.
        output = []
        for p in sequence:
            # Rotate the offsets.
            for i in range(len(offsets)):
                offsets[i] = (offsets[i] + 1) % 26
                if offsets[i] not in self.restarts[i]: break

            # enigma map = reflector**(rotor1**offset1 * rotor2**offset2 * ... * rotorN**offsetN * plugboard)
            c = p

            c = self.plugboard(c)
            for rotor, k in zip(self.rotors, offsets):
                shift = Permutation.from_shift(k)
                c = shift[rotor(shift(c))]

            c = self.reflector(c)

            for rotor, k in zip(reversed(self.rotors), reversed(offsets)):
                shift = Permutation.from_shift(k)
                c = shift[rotor[shift(c)]]
            c = self.plugboard[c]

            output.append(c)

        return ''.join(decode(x) for x in output)


if __name__ == '__main__':
    E = Enigma([II, V, III], B, 'AF-TV-KO-BL-RW', [{7}, {4}, {19}], [12, 2, 20])
    p = 'FOOBARBAZZZZ'
    assert p == E(E(p))
