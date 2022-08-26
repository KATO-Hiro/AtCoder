# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, op, b = input().rstrip().split(" ")

    if op == "?" or op == "=" or op == "!":
        print("error")
    elif op == "/":
        if b == "0":
            print("error")
        else:
            print(int(a) // int(b))
    else:
        print(eval(a + op + b))


if __name__ == "__main__":
    main()
