#!/usr/bin/env python3

import pandas as pd
import os
import regex as re

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

def is_prime(number, file):
    """Check if a number is prime

    It will check if a CSV file exists and check if the number is in that CSV file,
    if False, it will check if a number is divisible by any prime number in the CSV file.

    If the file does not exist, it will check if a number is divisible
    by all its previous numbers greater that one.

    Args:
        number: number to check if it is a prime or not.
        file: it is the name of the CSV file.

    Returns:
        True if the number is prime, False otherwise.
    """
    if os.path.isfile(file):
        df = pd.read_csv(file, index_col=0)

        if number in df.values:
            return True

        elif number < df.values.max():
            return False

        else:
            count = 0

            for value in df.values:
                if any(number % value == 0):
                    count += 1

            if count >= 1:
                return False
            else:
                return True
    else:
        count = 0
        for num in range(1, number + 1):
            if number % num == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False


def check_df(file):
    """Check if the CSV file exists

    Check if the CSV file exists, and it will create it if it doesn't find it.

    Args:
        file: it is the name of the CSV file.

    Returns:
        A DataFrame
    """
    if os.path.isfile(file):
        return pd.read_csv(file, index_col=0)

    else:
        df = pd.DataFrame()
        primos_list = []

        number = 2
        while len(primos_list) < 100:
            if is_prime(number, file):
                primos_list.append(number)
            number += 1
        df['1-100'] = primos_list
        df.to_csv(file)
        return df

def update_df(number_to_check, df, file):
    """Update the DataFrame

    Check if it is necessary to update the DataFrame.
    (if the number to check is less than the maximum number in the DataFram).

    It will keep updating the DataFrame and save it,
    until the number to check is less than the maximum.

    Args:
        number_to_check: The number to check.
        df: DataFrame
        file: it is the name of the CSV file.

    Returns:
        Nothings, but it will save the updated DataFrame in a CSV file.
    """

    if number_to_check > df.values.max():
        primos_list = []

        string = df.columns[-1]
        patter = r'(\d*)-(\d*)'
        result = re.search(patter, string)

        number = df.values.max() + 1

        while len(primos_list) < 100:
            if is_prime(number, file):
                primos_list.append(number)
            number += 1

        nume = int(result.group(2))
        colum_name = '{}-{}'.format(nume + 1, nume + 100)

        df[colum_name] = primos_list
        df.to_csv(file)

        if number_to_check > df.values.max():
            print('Updating DataFrame')
            return update_df(number_to_check, df, file)


def main():
    print('---------------------------------------------------------------------------')
    print('This program tell you if a number is Prime or Not. Follow the indications: ')
    print('---------------------------------------------------------------------------')
    number_to_check = get_number()
    print('---------------------------------------------------------------------------')
    file = 'primos.csv'
    df = check_df(file)
    update_df(number_to_check, df, file)
    df = check_df(file)

    if is_prime(number_to_check, file):
        print('{} is a PRIME NUMBER :)'.format(number_to_check))
    else:
        print('{} is NOT a Prime Number. :('.format(number_to_check))
    # print(df)
    # print(df.values)
    print(df)
    print(df.values.max())


main()
