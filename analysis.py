
from itertools import combinations, permutations, product
from string import ascii_uppercase
from heapq import nlargest

from progress.bar import Bar

from extensions.enigma import Enigma

def find_best(c, settings, label, count, top=1):
    with Bar(label, max=count, width=80, suffix='%(index)d/%(max)d %(eta)ds') as bar:
        return [setting for _, setting in nlargest(top, enumerate(settings), key=lambda X: (X[0] % 100 == 0 and bar.next(100)) or Enigma(*X[1]).score(c))]  #  fitness(Enigma(*X[1])(c)))]

def brute(c, available_rotors, num_rotors, available_reflectors, max_plugs):
    carry_sizes = [5, 20, 10, 10, 10, 5, 5]
    # Try all rotors and offsets.
    count = 26**num_rotors * sum(1 for _ in permutations(available_rotors, r=num_rotors))
    settings = (
        (reflector, rotors, offsets, tuple(0 for _ in range(num_rotors)), '')
        for reflector in available_reflectors
        for rotors in permutations(available_rotors, r=num_rotors)
        for offsets in product(range(26), repeat=num_rotors)
        )
    RESULTS = find_best(c, settings, '1) Rotors & Offsets', count, carry_sizes[0])
    for REFLECTOR, ROTORS, OFFSETS, _, _ in RESULTS:
        print(f'Found: {REFLECTOR}, {ROTORS}, {OFFSETS}, _, _')

    # Try all restarts.
    count = 26**len(ROTORS) * carry_sizes[0]
    settings = (
        (REFLECTOR, ROTORS, OFFSETS, rings, '')
        for REFLECTOR, ROTORS, OFFSETS, _, _ in RESULTS
        for rings in product(range(26), repeat=len(ROTORS))
        )
    RESULTS = find_best(c, settings, '2) Rings', count, carry_sizes[1])
    for REFLECTOR, ROTORS, OFFSETS, RINGS, _ in RESULTS:
        print(f'Found: {REFLECTOR}, {ROTORS}, {OFFSETS}, {RINGS}, _')

    # Try all plugboards.
    for index in range(max_plugs):
        count = (26 - 2 * index) * (25 - 2 * index) // 2 * carry_sizes[1+index]
        settings = (
            (REFLECTOR, ROTORS, OFFSETS, RINGS, PLUGBOARD+f'{i}{j}-')
            for REFLECTOR, ROTORS, OFFSETS, RINGS, PLUGBOARD in RESULTS
            for i, j in combinations(set(ascii_uppercase) - set(PLUGBOARD), r=2)
            )
        RESULTS = find_best(c, settings, f'3) Plug {index}', count, carry_sizes[2+index])

        for REFLECTOR, ROTORS, OFFSETS, RINGS, PLUGBOARD in RESULTS:
            print(f'Found: {REFLECTOR}, {ROTORS}, {OFFSETS}, {RINGS}, {PLUGBOARD}')

    return RESULTS

