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
    number = input('Enter an integer number: \n')

    while number.isnumeric() == False:
        number = input('{} is not a integer number. Try again: \n'.format(number))
    return int(number)

def is_prime(input_number, prime_array, file):
    """Check if a number is prime

    It will check if number is in prime_array, returning True, and if the number is not in prime_array,
    and it less that the maximum number in it. It will return False.

    otherwise will check if number is prime using prime_array.

    Args:
        number: number to check if it is a prime or not.
        prime_array: numpy array with the prime number.

    Returns:
        True if the number is prime, False otherwise.
    """

    if input_number in prime_array:
        return True

    elif input_number < prime_array.max():
        return False

    elif any(prime_array > np.sqrt(input_number)) == False:

        next_number = prime_array.max() + 1
        check_primes = np.array([])

        while any(prime_array > np.sqrt(input_number)) == False:

            new_array = set(prime_array) - set(check_primes)
            for prime in new_array:
                if input_number % prime == 0:
                    return False
                new_array = np.append(new_array,prime)


            count = 0
            for prime in prime_array[prime_array<=np.sqrt(next_number)]:
                if next_number % prime == 0:
                    count += 1
                    break

            if count == 0:
                prime_array = np.append(prime_array,next_number)
                save_array(file, prime_array)

            next_number += 1

        check_primes = np.array([])
        return True

    else:
        for prime in prime_array[prime_array <= np.sqrt(input_number)]:
            if input_number % prime == 0:
                return False
        return True


def load_prime_array(file):
    """Load prime_array file.

    It will check if primos.txt(file) exist returning True and the prime_array;
    False and None, otherwise.

    Args:
        file = name that the txt file has.

    Returns:
        Tupple (True, prime_array) or (False, None)
    """
    if os.path.isfile(file):
        prime_array = np.loadtxt(file, dtype=int)
        return prime_array

    else:
        return np.array([2])


def save_array(file, prime_array):
    """Save prime_array.

    It will save prime array in a txt file.

    Args:
        prime_array = numpy array with the prime numbers.
        file = name that the txt file will have.

    Returns:
        None
    """
    np.savetxt(file, prime_array, fmt='%d')


def main():
    file = 'primos.txt'
    print('---------------------------------------------------------------------------')
    print('This program will tell you if a number is Prime or Not.')
    print('You need to enter an integer number in the following step.')
    input_number = get_number()
    prime_array = load_prime_array(file)
    print('---------------------------------------------------------------------------')
    if is_prime(input_number, prime_array, file):
        print('{} is a PRIME NUMBER :)'.format(input_number))
    else:
        print('{} is NOT a Prime Number. :('.format(input_number))

main()
