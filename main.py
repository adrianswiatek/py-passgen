#!/usr/bin/env python3

import argparse
import pyperclip
import random
import string


def parse_args(default_length=20):
    total_length = default_length
    part_length = int(total_length / 5)

    parser = argparse.ArgumentParser(description="A simple password generator.")

    parser.add_argument(
        "-w", "--start-with", type=str, help="A first character in the password", required=False)
    parser.add_argument(
        "-l", "--length", type=int, help="Total length of the password", required=False, default=total_length)
    parser.add_argument(
        "-d", "--digits", type=int, help="Number of digits", required=False, default=part_length)
    parser.add_argument(
        "-u", "--uppercase", type=int, help="Number of uppercase characters", required=False, default=part_length)
    parser.add_argument(
        "-s", "--specials", type=int, help="Number of special characters", required=False, default=part_length)
    parser.add_argument(
        "-v", "--values", help="Prints values for all parameters", required=False, action="store_true")

    return parser.parse_args()


def draw_digits(amount):
    if amount == 0:
        return ""
    digits = string.digits
    random_index = random.randint(0, len(digits) - 1)
    return digits[random_index] + draw_digits(amount - 1)


def draw_specials(amount):
    if amount == 0:
        return ""

    specials = "!@#$%^&*"
    random_index = random.randint(0, len(specials) - 1)
    return specials[random_index] + draw_specials(amount - 1)


def draw_letters(amount):
    if amount == 0:
        return ""

    letters = string.ascii_letters.lower()
    random_index = random.randint(0, len(letters) - 1)
    return letters[random_index] + draw_letters(amount - 1)


def applying_uppercase(value, amount):
    if amount == 0 or len(value) == 0:
        return value

    indices = random_indices(value, amount)
    result = ""

    for index in list(range(len(value))):
        character = value[index]
        if index in indices:
            character = character.upper()
        result = result + character

    return result


def random_indices(value, amount, result=[]):
    if amount == 0 or len(value) == 0 or len(result) == len(value) - 1:
        return result

    random_index = random.randint(0, len(value) - 1)

    if random_index in result:
        return random_indices(value, amount, result)
    else:
        result.append(random_index)
        return random_indices(value, amount - 1, result)


def shuffled(value):
    value = list(value)
    random.shuffle(value)
    return "".join(value)


def generate_password(args):
    if args.length <= 0:
        return ""

    start_with = args.start_with[0] if args.start_with else ""

    digits = min(args.digits, args.length)
    specials = min(args.specials, args.length)

    number_of_letters = max(args.length - digits - specials, 0)
    letters = applying_uppercase(draw_letters(number_of_letters), args.uppercase)
    result = start_with + shuffled(letters + draw_digits(digits) + draw_specials(specials))

    return result[0:args.length]


def printValues(arguments):
    print()
    print(" Start with:\t", arguments.start_with)
    print(" Length:\t", arguments.length)
    print(" Digits:\t", arguments.digits)
    print(" Uppercase:\t", arguments.uppercase)
    print(" Specials:\t", arguments.specials)


if __name__ == '__main__':
    args = parse_args()

    password = generate_password(args)
    pyperclip.copy(password)

    print("\n", password)
    print("\n ---")
    print(" The password has been copied to the clipboard :)")

    if args.values:
        printValues(args)
