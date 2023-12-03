""" my attempt to the advent of code day 1 question 
"""
import re
from  pathlib import Path



BASE_DIR = Path(__file__).parent


regex_digits = re.compile(r"\d")  # find matching digits or value between [0-9]



inputs = [
    'xt36five77',
    'two8five6zfrtjj'
]



def get_calibration_value(text: str) -> int:
    digits = regex_digits.findall(text)
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(f"{first_digit}{last_digit}")



print(get_calibration_value(inputs[0]))





try:
    with open(BASE_DIR / 'calibration-document.txt', 'r') as inputs:
        # extracting data from the text file and storing as a list.
        letters_list = [list(input.rstrip()) for input in inputs]
        
        total_sum = 0   

        for letters in letters_list:
            # adding concat the digits
            num = []
            for index ,char  in enumerate(letters):  
                if char.isdigit():
                  num.append(char)
                  total_sum = total_sum + int(num[0] + num[-1])
        print(total_sum)

except Exception as exe:
    print(exe)


