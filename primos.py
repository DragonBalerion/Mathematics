#!/usr/bin/env python3

import os
import numpy as np


def get_number():
    """Get number from the user

    Ask the user to write a number until the user enters an integer number.

    Args:
        None

    Returns:
        An integer number.
    """
    number = input('enter an integer number to check if is a Prime Number or Not: \n')

    while number.isnumeric() == False:
        number = input('{} is not a integer number. Please, enter an integer number: \n'.format(number))
    return int(number)

def is_prime(number, prime_array):
    """Check if a number is prime

    It will check if number is in prime_array, returning True, and if the number is not in prime_array,
    and it less that the maximum number in it. It will return False.

    otherwise will update the prime_array.

    Args:
        number: number to check if it is a prime or not.
        prime_array: numpy array with the prime number.

    Returns:
        True if the number is prime, False otherwise.
    """

    if number in prime_array:
        return True

    elif number < prime_array.max():
        return False

def is_prime_array(number):
    """check if a number if prime, when creating the prime_array.

    It will check from 2 to the sqrt of number if number is divisible by any number in that range.

    Args:
        number: number to check if it is a prime or not.

    Returns:
        True if the number is prime, False otherwise.
    """
    count = 0
    for num in range(2, int(np.sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True

def check_list():
    """check if exist primos.txt.

    It will check if primos.txt exist, if not, it will create.
    Args:
        none

    Returns:
        prime_array
    """
    file = 'primos.txt'
    if os.path.isfile(file):
        prime_array = np.loadtxt(file, dtype=int)
    else:
        prime_array = np.array([])
        number = 2
        while len(prime_array) < 100:
            if is_prime_array(number):
                prime_array = np.append(prime_array, number)
            number += 1
    np.savetxt(file, prime_array, fmt='%d')
    return prime_array

def update_array(prime_array):
    """Update prime_array.

    It will update prime array, it will add 100 prime number to prime array, and it will save it in a txt file.

    Args:
        prime_array = numpy array with the prime numbers.

    Returns:
        prime_array
    """

    number = prime_array.max() + 1
    original_size_array = len(prime_array)
    file = 'primos.txt'
    number = prime_array.max()

    while len(prime_array) < original_size_array + 1000:
        count = 0
        for prime in prime_array[prime_array <= np.sqrt(number)]:
            if number % prime == 0:
                count += 1
                break
        if count == 0:
            prime_array = np.append(prime_array,number)
        number += 1
    np.savetxt(file, prime_array, fmt='%d')
    return prime_array

def update_array_until_number(number, prime_array):
    while number > prime_array.max():
        print('Updating prime_array ...')
        prime_array = update_array(prime_array)
    return prime_array


def main():
    print('---------------------------------------------------------------------------')
    print('This program tell you if a number is Prime or Not. Follow the indications: ')
    print('---------------------------------------------------------------------------')
    number = get_number()
    print('---------------------------------------------------------------------------')
    prime_array = check_list()
    prime_array = update_array_until_number(number, prime_array)
    print('---------------------------------------------------------------------------')
    print(prime_array)
    if is_prime(number, prime_array):
        print('{} is a PRIME NUMBER :)'.format(number))
    else:
        print('{} is NOT a Prime Number. :('.format(number))

main()
