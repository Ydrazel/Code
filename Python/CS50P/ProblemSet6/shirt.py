#-*- code: utf-8 -*-
import sys
from PIL import Image, ImageOps
from lines import FewArgumentsError,ManyArgumentsError

def main():
    if assert_input():
        apply()

def assert_input():
    while True:
        try:
            if len(sys.argv) < 3:
                raise FewArgumentsError
            elif len(sys.argv) > 3:
                raise ManyArgumentsError
            elif not open(sys.argv[1]).name.endswith(".jpg"):
                raise TypeError
            else:
                return open(sys.argv[1])
        except FewArgumentsError:
            sys.exit("Too few command-line arguments.")
        except ManyArgumentsError:
            sys.exit("Too many command-line arguments.")
        except TypeError:
            sys.exit("Invalid input.")
        except FileNotFoundError:
            sys.exit("Input file does not exist")

def apply():
    with Image.open(sys.argv[1]) as im:
        im_cropped = ImageOps.fit(im, (600, 600))
        iim = Image.open(sys.argv[2])
        im_cropped.paste(iim, iim) 
        im_cropped.save("output.png")

if __name__ == "__main__":
    main()
