"""
Prints statistics about mistakes that are made when checking if elements of one DB are elements of another (hashed) DB.
The simulation parameters are defined in the programs constants.
(Mistakes = false-positive calls)

Instructions:
1. Define the simulations parameters - which are the 1st 4 constants of this program.
2. Run simulation.

Imports:
"mmh3" was downloaded from: https://pypi.org/project/mmh3/
"rand-String" was downloaded from: https://pypi.org/project/rand-string/
"""
import random

import rand_string.rand_string as rand
import mmh3

# The amount of hash functions used to hash/hash-check each element.
HASH_AMOUNT = 13
# The size of the hashing table.
TABLE_SIZE = 32000000
# The size of the randomly generated DB to be hashed into table.
DB_SIZE = 1000000
# The amount of checks that would be made against the hashing table with elements that are NOT in the DB.
SAMPLE_SIZE = 50000

# Determines the length of each element in the DB. (changing is not recommended)
DB_ELEMENT_LEN = 6
# Determines the MINIMAL length of each of the not-in-DB elements. (must be > DB_ELEMENTS_LEN!)
FALSE_MIN_SIZE = DB_ELEMENT_LEN + 1
# Determines the MINIMAL length of each of the not-in-DB elements. (must be >= FALSE_MIN_SIZE)
FALSE_MAX_SIZE = FALSE_MIN_SIZE + 2
# Creates the empty hash table.
TABLE = [0] * TABLE_SIZE


def rand_string(shortest, longest):
    """
    Creates a string of random ASCII characters - at a length within a given range.

    :param shortest: Minimal length of string.
    :param longest: Maximal length of string.
    :return: Random string.
    """

    return rand.RandString("ascii", random.randint(shortest, longest))


def fill_table(db_size, table, hash_amount):
    """
    Hashes into table a randomly created data-base.

    :param db_size: The size of the data base.
    :param table: The table to hash the DB into.
    :param hash_amount: How many hash functions should be used for the process.
    """
    print(f'Hashing the {db_size} long - randomly created DB into the table...\n')
    for i in range(1, db_size):
        element = rand_string(1, DB_ELEMENT_LEN)
        for hash_func in range(1, hash_amount):
            hash_val = mmh3.hash(element, hash_func) % len(table)
            table[hash_val] = 1
    print("Data base hashing - DONE.\n")


def hashes_match(element, table, hash_amount):
    """
    :param element: An element to check.
    :param table: A hashing table to check against.
    :param hash_amount: The amount of hashing functions to be used in the checking process.
    :return: If the hash values of the element only matches indexes of elements from table whose values are 1.
    """
    for i in range(1, hash_amount):
        hash_val = mmh3.hash(element, i) % len(table)
        if table[hash_val] == 0:
            return False
    return True


def count_mistakes(elements_amount, table, hash_amount):
    """
    Checks how many elements of a randomly generated data-base are positive for hash_check().

    :param elements_amount: The amount of elements to check.
    :param table: The table to check the DB against.
    :param hash_amount: How many hash functions should be used for the process.
    :return: Amount of positives.
    """
    print(f"Preforming the check against {elements_amount} elements that are NOT in the original DB...\n")
    count = 0
    for i in range(1, elements_amount):
        falsy = rand_string(FALSE_MIN_SIZE, FALSE_MAX_SIZE)
        if hashes_match(falsy, table, hash_amount):
            count = count + 1
    print("Check done.\n")
    return count


def calc_percentage(sample_size, mistakes_amount):
    """
    :return: The percentage of mistakes made out of the total sample size.
    """
    return (mistakes_amount / sample_size) * 100


def calc_formula(m, N, K):
    """
    Calculates the formula from question b.
    Excuse us for the ugliness.

    :param m: Table size.
    :param N: DB size.
    :param K: Hash amount.
    :return: Value of formula.
    """
    formula_val = (1 - (1 - (1 / m)) ** (K * N)) ** K
    val_in_percents = formula_val * 100
    return val_in_percents


def print_summary(sample_size, mistakes_amount, percentage, table_size, formula_val):
    """
    Prints the summary of the simulation.

    :param sample_size: Amount of non-DB elements used to preform the check.
    :param mistakes_amount: Total amount of false-positive calls made during check.
    :param percentage: The percentage of mistakes out of the non-DB size.
    :param table_size: the size of the hashing table.
    :param formula_val: The prediction made by the formula from question b.
    """
    print(f"THE RESULTS:\n"
          f"Out of {sample_size} elements checked\n"
          f"against the {table_size} long hash table,\n"
          f"{mistakes_amount} false answers were made,\n"
          f"which are {percentage}% of the over-all amount of checks.\n"
          f"In comparison, the expected mistakes percentage made should be, by the formula: {formula_val}%\n"
          f"the difference between the current test and the formulas prediction is: {abs(percentage - formula_val)}%\n\n"
          f"Thanks and have a good day :)")


def main():
    fill_table(DB_SIZE, TABLE, HASH_AMOUNT)
    mistakes_amount = count_mistakes(SAMPLE_SIZE, TABLE, HASH_AMOUNT)
    percentage = calc_percentage(SAMPLE_SIZE, mistakes_amount)
    formula = calc_formula(TABLE_SIZE, DB_SIZE, HASH_AMOUNT)
    print_summary(SAMPLE_SIZE, mistakes_amount, percentage, TABLE_SIZE, formula)


if __name__ == '__main__':
    main()
