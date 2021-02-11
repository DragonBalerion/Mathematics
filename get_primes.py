#!/usr/bin/env python3

import numpy as np
from decimal import Decimal as dcm

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

def open_or_create_prime_nparray():
    """open or create a numpy array with prime numbers.

    if prime_numbers.npy exits it will open it, otherwise it will create it.

    Args:
        None

    Returns:
        A Numpy array with prime numbers.
    """

    try:
        return np.load("prime_numbers.npy")

    except:
        np.save("prime_numbers.npy", np.array([2,3]))
        return open_or_create_prime_nparray()


def update_prime_nparray(input_number, sqrt_inumber):
    """Update the prime numbpy array.

    It will check if the maximun prime number in the array plus two is prime
    or not until the new lenght is 1000 bigger than before.

    Args:
        input_number: It is the number we need to check if it is prime or not.
        sqrt_inumber: it is the square root of input_number.

    Returns:
        the is_prime function to check if input_number is prime.
    """

    global prime_numbers
    global max_prime_old
    number = prime_numbers.max() + 2
    prime_old = prime_numbers.max()
    len_prime = len(prime_numbers)
    print("Addind 1000 prime numbers to the Numpy array. The maximun is {}".format(prime_numbers.max()))
    while len(prime_numbers) < len_prime + 1000:
        max_prime_old = 0
        if is_prime(number) == True:
            prime_numbers = np.append(prime_numbers, number)
        number += 2
    max_prime_old = prime_old
    print("Saving ...")
    np.save("prime_numbers.npy", prime_numbers)
    return is_prime(input_number)

def is_prime(input_number):
    """checks if a number is prime or not.

    It will check if a number is prime in four steps.
        1. checks if input_number is a perfect square.
        2. checks if input_number is less than or equal to the maximun number in
            the numpy array prime_numbers and if it in the prime_numbers array.
        3. checks if possible if input_number is divisible by any prime number
            less than or equal to the square root of input_number.
        4. checks if input_number is divisible by any prime number in
            prime_numbers.
    Args:
        input_number: It is the number we need to check if it is prime or not.

    Returns:
        True  -- if input_number is a prime number.
        Flase -- if input_number is NOT a prime number.
        update_prime_nparray -- when it cannot decide whether or not
                                input_number is prime.

    """

    global prime_numbers
    global max_prime_old
    input_number = int(input_number)
    sqrt_inumber = dcm.sqrt(dcm(input_number))
    sqrt_inumber_int = int(sqrt_inumber)

    if sqrt_inumber % 1 == 0:
        return False

    elif input_number <= prime_numbers.max():
        if input_number in prime_numbers:
            return True
        return False


    elif sqrt_inumber_int <= max(prime_numbers):
        for p_number in prime_numbers[prime_numbers <= sqrt_inumber_int]:
            if input_number % p_number == 0:
                return False
        return True

    else:
        if max_prime_old == 0:
            for p_number in prime_numbers:
                if input_number % p_number == 0:
                    return False
            return update_prime_nparray(input_number, sqrt_inumber_int)
        else:
            for p_number in prime_numbers[prime_numbers > max_prime_old]:
                if input_number % p_number == 0:
                    return False
            return update_prime_nparray(input_number, sqrt_inumber_int)


#Global Variable - prime_numbers
prime_numbers = open_or_create_prime_nparray()

def main():
    global prime_numbers
    global max_prime_old
    max_prime_old = 0
    prime_numbers = open_or_create_prime_nparray()
    input_number = get_number()
    x = is_prime(input_number)
    if x == True:
        print("{} is a PRIME NUMBER".format(input_number))
    else:
        print("{} is NOT a prime number".format(input_number))
    print("Bye :)")

if __name__ == '__main__':
    main()
