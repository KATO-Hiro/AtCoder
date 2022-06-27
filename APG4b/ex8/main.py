# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    p = int(input())

    if p == 1:
        price = int(input())   
        n = int(input())
        print(price * n)
    else:
        text = input().rstrip()
        price = int(input())   
        n = int(input())
        print(text + "!")
        print(price * n)


if __name__ == "__main__":
    main()
