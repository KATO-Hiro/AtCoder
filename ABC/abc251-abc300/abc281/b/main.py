# -*- coding: utf-8 -*-


def main():
    import re
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    pattern = "[A-Z][1-9][0-9]{5}[A-Z]"

    r = re.compile(pattern)
    result = r.match(s)

    if result:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
