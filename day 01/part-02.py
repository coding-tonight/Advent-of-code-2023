from pathlib import Path
from functools import reduce


BASE_DIR = Path(__file__).parent

keywords = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def findKeyWord(text: str):
    filter_values = [ value 
                     for keywords, value in keywords.items() 
                     if keywords in text ]
    
   
    first_digits = filter_values[0]
    last_digits = filter_values[-1]
    return filter_values
    # return f'{first_digits}{last_digits}'



print(findKeyWord('eightwothree'))






def main():
    try:
        with open(BASE_DIR / 'calibration-document.txt', 'r') as file:
           calibration_values = [ int(calibration_value) 
                                 for line in  file 
                                 for calibration_value in [findKeyWord(line)] 
                                 if calibration_value is not None]
            
           total_sum = sum(calibration_values)
           return total_sum

    except Exception as exe:
        print(exe)



# print(main())
