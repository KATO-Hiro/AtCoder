# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, op, b = input().rstrip().split()
    a, b = int(a), int(b)

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("error")
        else:
            print(a // b)
    else:
        print("error")


if __name__ == "__main__":
    main()
