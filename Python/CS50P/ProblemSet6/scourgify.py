#-*- code: utf-8 -*-
import sys
import csv
from lines import FewArgumentsError, ManyArgumentsError

def main():
    assert_input()
    convert()

def assert_input():
    while True:
        try:
            if len(sys.argv) < 3:
                raise FewArgumentsError
            elif len(sys.argv) > 3:
                raise ManyArgumentsError
            elif not (open(sys.argv[1])).name.endswith(".csv"):
                raise TypeError
            else:
                return open(sys.argv[1], mode="r")
        except FewArgumentsError:
            sys.exit("Too few command-line arguments.")
        except ManyArgumentsError:
            sys.exit("Too many command-line arguments.")
        except TypeError:
            sys.exit("Input file is not a CSV file.")
        except FileNotFoundError:
            sys.exit("Input file does not exist")

def convert():
    with open(sys.argv[1], mode="r") as input_file:
        with open(sys.argv[2], mode="a") as output_file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            students = csv.DictReader(input_file)
            for row in students:
                last, first = (row['name'].split(", "))
                house = (row['house'])
                writer.writerow({'first': first, 'last': last, 'house': house})

if __name__ == "__main__":
    main()
