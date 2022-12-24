# -*- coding: utf-8 -*-


def is_met_conditions_using_regular_expressions(strings, pattern):
    # See:
    # https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3
    # https://atcoder.jp/contests/abc281/submissions/37139022

    import re

    r = re.compile(pattern)
    result = r.fullmatch(strings)

    if result:
        return "Yes"
    else:
        return "No"


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    pattern = r"[A-Z][1-9]\d{5}[A-Z]"

    print(is_met_conditions_using_regular_expressions(s, pattern))
    

if __name__ == "__main__":
    main()
