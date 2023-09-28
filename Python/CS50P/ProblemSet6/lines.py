#-*- code: utf-8 -*-
import sys

class FewArgumentsError(Exception):
    pass
class ManyArgumentsError(Exception):
    pass

def main():
    file = assert_input()
    print(line_count(file))

def assert_input():
    while True:
        try:
            if len(sys.argv) < 2:
                raise FewArgumentsError
            elif len(sys.argv) > 2:
                raise ManyArgumentsError
            elif not (open(sys.argv[1])).name.endswith(".py"):
                raise TypeError
            else:
                return open(sys.argv[1], mode="r")
        except FewArgumentsError:
            sys.exit("Too few command-line arguments.")
        except ManyArgumentsError:
            sys.exit("Too many command-line arguments.")
        except TypeError:
            sys.exit("Not a python file.")
        except FileNotFoundError:
            sys.exit("File does not exist")

def line_count(file):
    line_count = 0
    for line in file:
        if line.isspace() or (line.lstrip()).startswith("#"):
            pass
        else:
            line_count += 1
    return line_count

if __name__ == "__main__":
    main()
