"""
xkcd

Script that generates random sequence of alphabet in specified length. Keeps log of character codes. Does not repeat existing code. Use for unique project code generation

Author: Nic La
Last Edit: June 2022
"""


import logging
import random


# Uncomment to display logging
# logging.basicConfig(level=logging.DEBUG)


attempt_limit = 100
log_file = 'log.txt'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def generate_code(user_input):
    """Generates random code based on user input"""
    global alphabet
    rand_code = ''
    for num in range(user_input):
        rand_code += random.choice(alphabet)
    return rand_code


def check_log():
    """Open log file and note existing codes"""
    global log_file
    with open(log_file, 'r') as log:
        log_raw = log.readlines()
        codes = [line.strip() for line in log_raw]
    return codes


def update_log(new_code):
    """Add new code to log file"""
    global log_file
    with open(log_file, 'a') as log:
        log.write(new_code + '\n')


if __name__ == '__main__':
    # Accept user input
    user_input = ''
    while not(user_input.isnumeric()):
        user_input = input('Enter length: ')

    # Compare code against log and repeat until unique code
    old_codes = check_log()
    unique = False
    count = 1
    while not(unique) and (count < attempt_limit):
        new_code = generate_code(int(user_input))
        for old_code in old_codes:
            if new_code == old_code:
                unique = False
                count += 1
                logging.debug(f'New code, {new_code}, was NOT unique!')
                break
            unique = True
    logging.debug(f'Attempts = {count}')

    if count < attempt_limit:
        # Update log with new code
        update_log(new_code)

        # Print new code
        print(f'New code = {new_code}')
    else:
        print(f'New code generation failed with {count} attempts')
