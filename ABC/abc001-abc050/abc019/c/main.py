# -*- coding: utf-8 -*-


def mod2(number: int):
    while True:
        if number % 2 == 0:
            number //= 2
        else:
            return number


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = set()

    for ai in a:
        ans.add(mod2(ai))

    print(len(ans))


if __name__ == "__main__":
    main()
