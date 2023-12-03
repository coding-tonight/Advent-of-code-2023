""" my attempt to the advent of code day 1 question 
"""
import re
from pathlib import Path


BASE_DIR = Path(__file__).parent


regex_digits = re.compile(r"\d")  # find matching digits or value between [0-9]


def get_calibration_value(text: str):
    try:
        digits = regex_digits.findall(text)
        first_digit = digits[0]
        last_digit = digits[-1]
        return int(f"{first_digit}{last_digit}")

    except:
        print(f"{text} does not match with regex")


# print(get_calibration_value(inputs[0]))


def main():
    # extract data first and last digits for the text the calculate the total sun of the
    try:
        with open(BASE_DIR / 'calibration-document.txt', 'r') as file:
            # extracting data from the text file and storing as a list.
            calibration_list = [
                value
                for line in file
                for value in [get_calibration_value(line)]
                if value is not None]

            total_sum = sum(calibration_list)
            return total_sum

    except Exception as exe:
        print(exe)


if __name__ == '__main__':
    print(main())
