#!/usr/bin/env python3

import os
import pandas as pd
import numpy as np


file = 'primos.txt'
file_csv = 'primos.csv'
if os.path.isfile(file):
    prime_array = np.loadtxt(file, dtype=int)
else:
    print('There is no {} file.'.format(file))
print(prime_array)

def convert_to_DataFrame(prime_array):
    start = 1
    end = 100
    n_columns_names = []
    n_columns = int(len(prime_array) / 100)
    if n_columns < len(prime_array) / 100:
        n_columns += 1

    for column in range(1, n_columns + 1):
        name = '{} to {}'.format(start, end)
        n_columns_names.append(name)
        start += 100
        end += 100

    primes_100 = []
    primes = []
    count = 0
    for prime in prime_array:
        count += 1
        primes.append(prime)
        if count == 100:
            primes_100.append(primes)
            primes = []
            count = 0
    if count != 0:
        primes_100.append(primes)


    for prime in primes_100:
        while len(prime) < 100:
            prime.append('/')

    df = pd.DataFrame()

    for name, prime in zip(n_columns_names, primes_100):
        df[name] = prime
    df.to_csv(file_csv)
    print('DataFrame saved ... :)')

def main():
    convert_to_DataFrame(prime_array)

main()
