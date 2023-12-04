from pathlib import Path


BASE_DIR = Path(__file__).parent

keywords = {
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


def findKeywords(text: str):
    pass


# main function
def main():
    try:
        with open(BASE_DIR / 'calibration-document.txt', 'r') as file:
            calibration_values = [line for line in file]

            print(calibration_values)

    except Exception as exe:
        print(exe)


main()
