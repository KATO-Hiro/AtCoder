# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    d = int(input())
    a = input().rstrip().split(".")
    b = input().rstrip().split(".")
    # print(a)
    # print(b)

    c = int(a[0]) + int(b[0])
    e = int(a[1]) + int(b[1])

    if len(list(str(e))) > d:
        c += 1
        e = str(e)[1:]

    # print(c)
    # print(e)
    print(str(c) + "." + str(e))


if __name__ == "__main__":
    main()
