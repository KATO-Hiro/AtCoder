# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = int(input())

    for i in range(n):
        op, bi = input().rstrip().split()
        bi = int(bi)

        if op == "+":
            a += bi
        elif op == "-":
            a -= bi
        elif op == "*":
            a *= bi
        else:
            if bi == 0:
                print("error")
                break

            a //= bi

        print(i + 1, a)


if __name__ == "__main__":
    main()
