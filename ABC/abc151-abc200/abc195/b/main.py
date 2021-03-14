# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, w = map(float, input().split())
    a = int(a)
    b = int(b)
    w = int(w) * 1000

    value_min = float("inf")
    value_max = -float("inf")

    for i in range(1, 10 ** 6 + 1):
        if a * i <= w <= b * i:
            value_min = min(value_min, i)
            value_max = max(value_min, i)

    if value_min == float("inf"):
        print("UNSATISFIABLE")
    else:
        print(value_min, value_max)


if __name__ == "__main__":
    main()
