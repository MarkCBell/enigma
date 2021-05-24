
from collections import Counter
from itertools import combinations, permutations, product, islice
from string import ascii_uppercase
import heapq
import os
import multiprocessing as mp

from extensions.enigma import Enigma

INDEX = int(os.environ.get('AWS_BATCH_JOB_ARRAY_INDEX', 0))
CIPHERTEXT = os.environ['CIPHER'].replace(' ', '').upper()
BATCH_SIZE = int(os.environ.get('BATCH_SIZE', 1))

def score(setting):
    # plaintext = Enigma(*setting)(CIPHERTEXT)
    # return sum(v**2 for v in Counter(plaintext).values())
    return Enigma(*setting).score(CIPHERTEXT)

def nlargest(n, settings, key):
    # A parallel version of:
    #   return heapq.nlargest(n, settings, key)
    # Map:
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.starmap(heapq.nlargest, ((n, chunk, score) for chunk in iter(lambda: list(islice(settings, 10000)), [])))

    # Reduce:
    return heapq.nlargest(n, (item for result in results for item in result), key)

if __name__ == '__main__':
    CARRY_SIZES = [5, 20, 10, 10, 10, 5, 5]
    REFLECTOR = 0

    # Try all rotors and offsets.
    settings = (
        (REFLECTOR, rotors, offsets, (0, 0, 0), '')
        for rotors in permutations(range(4), r=3)
        for offsets in product(range(26), repeat=3)
        )
    # Filter for each batch
    settings = (setting for index, setting in enumerate(settings) if index % BATCH_SIZE == INDEX)
    RESULTS = nlargest(CARRY_SIZES[0], settings, key=score)

    # Try all rings.
    settings = (
        (REFLECTOR, ROTORS, OFFSETS, rings, '')
        for REFLECTOR, ROTORS, OFFSETS, _, _ in RESULTS
        for rings in product(range(26), repeat=len(ROTORS))
        )
    RESULTS = nlargest(CARRY_SIZES[1], settings, key=score)

    # Try all plugboards.
    for index in range(5):
        settings = (
            (ROTORS, REFLECTOR, OFFSETS, RINGS, PLUGBOARD+f'{i}{j}-')
            for ROTORS, REFLECTOR, OFFSETS, RINGS, PLUGBOARD in RESULTS
            for i, j in combinations(set(ascii_uppercase) - set(PLUGBOARD), r=2)
            )
        RESULTS = nlargest(CARRY_SIZES[2+index], settings, key=score)

    for setting in RESULTS:
        print(score(setting), setting, Enigma(*setting)(CIPHERTEXT))

