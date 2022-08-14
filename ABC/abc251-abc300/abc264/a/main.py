# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = "atcoder" 
    l, r = map(int, input().split())
    l -= 1
    print(s[l:r])


if __name__ == "__main__":
    main()
