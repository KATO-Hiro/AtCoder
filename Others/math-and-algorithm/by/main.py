# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    # See:
    # https://atcoder.jp/contests/math-and-algorithm/submissions/28314458
    if c == 1:
        print("No")
    elif a < pow(c, min(b, 60)):
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
