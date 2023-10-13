import sys
import re
def main():
    s = input("Hour: ").lower()
    m = re.search(r'^(\d*?):?(\d*)?\s+(.*?)\s+to\s+(\d*?):?(\d*)?\s+(.*?)$', s)
    fc = re.search(r'(:+?)', s)
    if fc != None:
        sh,sm,sp,fh,fm,fp = m.groups()
        return (sh, sm, sp, fh, fm, fp)
    else:
        _,sh,sp,_,fh,fp = m.groups()
        return (sh, sp, fh, fp)
print(main())
