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
    s = input("Hour: ").lower()
    m = re.search(r'^(\d*?):?(\d*)?\s+(.*?)\s+to\s+(\d*?):?(\d*)?\s+(.*?)$', s)
    fc = re.search(r'(:+?)', s)
    if fc != None:
        sh,sm,sp,fh,fm,fp = m.groups()
        start = [sh, sp , sm]
        finish = [fh, fp, fm]
#        return (start, finish)
    else:
        _,sh,sp,_,fh,fp = m.groups()
        start = [sh, sp]
        finish = [fh, fp]
#        return (start, finish)
    
    st = Convert.conv(start)
    fn = Convert.conv(finish)
    return (st, fn)

print(main())