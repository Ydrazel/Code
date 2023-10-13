#-*- code: utf-8 -*-
import sys
import re

class Convert:
    def __init__(self, lst):
        self.lst = lst
    def conv(self):
        if self[1] == 'am':
            if self[0] == '12':
                self[0] = '00'
                return self
            else:
                return self
        else:
            if self[0] == '12':
                return self
            else:
                self[0] = int(self[0]) + 12
                return self

def main():
    print(convert(input("Hours: ").lower()))

def convert(s):
    m = re.search(r'^(\d*?):?(\d*)?\s+(.*?)\s+to\s+(\d*?):?(\d*)?\s+(.*?)$', s)
    while True:
        try:
            if m == None:
                raise ValueError
            fc = re.search(r'(:+?)', s)
            if fc != None:
                sh,sm,sp,fh,fm,fp = m.groups()
                if sm == '60' or fm == '60':
                    raise ValueError
                start = Convert.conv([sh, sp , sm])
                finish = Convert.conv([fh, fp, fm])
                return f"{int(start[0]):02}:{int(start[2]):02} to {int(finish[0]):02}:{int(finish[2]):02}"
            else:
                _,sh,sp,_,fh,fp = m.groups()
                start = Convert.conv([sh, sp])
                finish = Convert.conv([fh, fp])
                return f"{int(start[0]):02}:00 to {int(finish[0]):02}:00"
        except ValueError:
            sys.exit("Value Error!")

if __name__ == "__main__":
    main()