# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    result1 = (s.rfind("B") - s.find("B")) % 2 == 1
    result2 = s.find("R") < s.find("K") < s.rfind("R")

    # See:
    # https://atcoder.jp/contests/abc297/editorial/6178
    if result1 and result2:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
