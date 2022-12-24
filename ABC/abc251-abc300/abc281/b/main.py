# -*- coding: utf-8 -*-


def main():
    import re
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    pattern = "[A-Z]{1}[0-9]{6}[A-Z]{1}"

    r = re.compile(pattern)
    result = r.match(s)

    if result:
        if len(list(str(int(s[1:7])))) == 6:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
