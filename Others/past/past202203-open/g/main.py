# -*- coding: utf-8 -*-


def f(a, b, c, x):
    return (a * (x ** 5) + b * x + c)


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    lower = 1.0
    upper = 2.0

    while upper - lower > 10 ** -12:
        mid = (lower + upper) / 2
        result = f(a, b, c, mid) 

        if result > 0:
            upper = mid
        elif result < 0:
            lower = mid
        else:
            print(mid)
            exit()
    
    print(lower)


if __name__ == "__main__":
    main()
