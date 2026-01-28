# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = a[::-1]
    b = b[::-1]

    while a:
        while b and b[-1] != a[-1]:
            b.pop()

        if len(b) == 0:
            break

        a.pop()
        b.pop()

    if len(a) == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
