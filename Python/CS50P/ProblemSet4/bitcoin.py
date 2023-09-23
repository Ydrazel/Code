#-*- code: utf-8 -*-
import sys
import json
import requests

def main():
    amount = assert_input()
    data = request_value().json()
    rate = data['bpi']['USD']['rate_float']
    print(f"${(amount * rate):,.4f}")

def assert_input():
    while True:
        try:
            if sys.argv[1]:
                return float(sys.argv[1])
            else:
                pass
        except IndexError:
            sys.exit("Missing command-line argument")
        except ValueError:
            sys.exit("Command-line argument is not a number")
        except (KeyError,TypeError):
            sys.exit("Something else went wrong!")

def request_value():
    while True:
        try:
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            return r
        except requests.RequestException:
            sys.exit("A request exception occured")

if __name__ == "__main__":
    main()
