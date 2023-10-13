#-*- code: utf-8 -*-
import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    m = re.split('\.', ip)
    for element in m:
        if any((re.match('(^\D+$)', element)) for element in m):
            return False
        elif any(int(element) not in range(0,256) for element in m):
            return False
        else:
            return True
                
if __name__ == "__main__":
    main()
