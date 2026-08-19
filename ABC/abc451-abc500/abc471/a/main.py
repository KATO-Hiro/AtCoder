# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    ok = False

    if a + b == 9:
        ok = True
    elif a - b == 9:
        ok = True
    elif a * b == 9:
        ok = True
    elif a == 9 * b:
        ok = True

    if ok:
        print("Nine")
    else:
        print("Nein")


if __name__ == "__main__":
    main()
