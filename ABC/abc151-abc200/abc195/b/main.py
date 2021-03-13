# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, w = map(float, input().split())
    a = int(a)
    b = int(b)
    w = int(w) * 1000

    if w % a != 0 and w % b != 0 and (w // a == w // b):
        print("UNSATISFIABLE")
    else:
        print(((w + b - 1) // b), w // a)


if __name__ == "__main__":
    main()
