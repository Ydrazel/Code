#-*- code: utf-8 -*-
import csv
import sys
from tabulate import tabulate
from lines import FewArgumentsError, ManyArgumentsError

def main():
    file = assert_input()
    print(tabular(file))

def assert_input():
    while True:
        try:
            if len(sys.argv) < 2:
                raise FewArgumentsError
            elif len(sys.argv) > 2:
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
            sys.exit("Not a CSV file.")
        except FileNotFoundError:
            sys.exit("File does not exist")

def tabular(file):
    table = csv.DictReader(file)
    return (tabulate(table, tablefmt="grid"))

if __name__ == "__main__":
    main()
