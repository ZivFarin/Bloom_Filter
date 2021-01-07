"""
Prints what elements from CHECK_FILE are recognized, through a hashing database, as elements of the DB_FILE.
"""

import mmh3

# The file to be inserted to the hashing table.
DB_FILE = "evens.txt"
# The file to check against the hashing table.
CHECK_FILE = "all.txt"

# The length of the hashing table.
TABLE_LENGTH = 32000000
# The amount of hash functions used to hash & hash-check each element.
HASH_AMOUNT = 13


def inserts(data_base, table, hash_amount):
    """
    Inserts '1's into the appropriate places in the table (according to the hashes) for a given data_base.
    Runtime: O(hash_amount * O(murmurhash)) * |Inputs| = O(hash_amount * O(1)) * |Inputs| = O(hash_amount * |Inputs|)

    :param data_base: List of elements to hash into the table.
    :param table: A list to hash the DB into.
    :param hash_amount: How many hash functions would be used in the process.
    """
    for element in data_base:
        for i in range(1, hash_amount):
            hash_val = mmh3.hash(element, i) % len(table)
            table[hash_val] = 1


def hash_check(element, table, hash_amount):
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


def check(check_list, table, hash_amount):
    """
    For every element in check_list, prints if it is positive for hash_check.
    Runtime: O(hash_amount * |check_list|)

    :param check_list: List of elements to check.
    :param table: The hash table that the elements from "check_list" would be checked against.
    :param hash_amount: How many hash functions would be used in the process.
    """
    for element in check_list:
        if hash_check(element, table, hash_amount):
            print(f"{element} is in the database")
        else:
            print(f"{element} is not in the database")


def pars_file(file_name):
    """
    Parses the given file, by commas, into a list of strings.
    Runtime: O(characters in file)

    :param file_name: Name of the file.
    :return: The aforementioned list.
    """
    return open(file_name).read().split(",")


def main():
    table = [0] * TABLE_LENGTH
    db_list = pars_file(DB_FILE)
    inserts(db_list, table, HASH_AMOUNT)
    checks_list = pars_file(CHECK_FILE)
    check(checks_list, table, HASH_AMOUNT)


if __name__ == '__main__':
    main()
