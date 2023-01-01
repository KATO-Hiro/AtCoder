# -*- coding: utf-8 -*-


def main():
    from string import ascii_uppercase
    import sys

    input = sys.stdin.readline

    k = int(input())
    alpha = ascii_uppercase
    print(alpha[:k])
    

if __name__ == "__main__":
    main()
