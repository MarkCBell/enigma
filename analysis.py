
from itertools import combinations, permutations, product
from collections import Counter
from string import ascii_uppercase

from progress.bar import Bar

from enigma import Enigma

def fitness(strn):
    n = len(strn)
    histogram = Counter(strn)
    return sum(v * (v-1) for v in histogram.values()) / (n * (n-1))

def find_best(c, settings, label, count):
    with Bar(label, max=count, width=80, suffix='%(index)d/%(max)d %(eta)ds') as bar:
        return max(enumerate(settings), key=lambda X: (X[0] % 100 == 0 and bar.next(100)) or fitness(Enigma(*X[1])(c)) )[1]
    return max(enumerate(settings), key=lambda X: fitness(Enigma(*X[1])(c)) )[1]

def brute(c, available_rotors, num_rotors, REFLECTOR, max_plugs):
    # Try all rotors and offsets.
    count = 26**num_rotors * sum(1 for _ in permutations(available_rotors, r=num_rotors))
    settings = (
        (rotors, REFLECTOR, '', [{0} for _ in range(num_rotors)], offsets)
        for rotors in permutations(available_rotors, r=num_rotors)
        for offsets in product(range(26), repeat=num_rotors)
        )
    ROTORS, _, _, _, OFFSETS = find_best(c, settings, '1) Rotors & Offsets', count)
    print(f'Found: {ROTORS=}, {OFFSETS=}\n')

    # Try all restarts.
    count = 26**len(ROTORS)
    settings = (
        (ROTORS, REFLECTOR, '', [{restart} for restart in restarts], OFFSETS)
        for restarts in product(range(26), repeat=len(ROTORS))
        )
    _, _, _, RESTARTS, _ = find_best(c, settings, '2) RESTARTS', count)
    print(f'Found: {RESTARTS=}\n')

    # Try all plugboards.
    plugboard = ''
    for index in range(max_plugs):
        available = set(ascii_uppercase) - set(plugboard)
        count = sum(1 for _ in combinations(available, r=2))
        settings = (
            (ROTORS, REFLECTOR, plugboard+f'{i}{j}-', RESTARTS, OFFSETS)
            for i, j in combinations(available, r=2)
            )
        _, _, plugboard, _, _ = find_best(c, settings, f'3) PLUG {index}', count)

    PLUGBOARD = plugboard[:-1]  # Drop the trailing -.
    print(f'Found: {PLUGBOARD=}\n')

    return ROTORS, REFLECTOR, PLUGBOARD, RESTARTS, OFFSETS

