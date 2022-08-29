# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = int(input())

    for i in range(1, n + 1):
        op, b = input().rstrip().split(" ")
        b = int(b)

        if op == "+":
            a += b
        elif op == "-":
            a -= b
        elif op == "*":
            a *= b
        elif op == "/" and b != 0:
            a = int(a / b)
        else:
            print("error")
            break

        print(str(i) + ":" + str(a))


if __name__ == "__main__":
    main()
