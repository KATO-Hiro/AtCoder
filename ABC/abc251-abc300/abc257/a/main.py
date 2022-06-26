# -*- coding: utf-8 -*-


def main():
    from string import ascii_uppercase
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    s = ""

    for alpha in ascii_uppercase:
        for i in range(n):
            s += alpha
    
    print(s[x - 1])


if __name__ == "__main__":
    main()
