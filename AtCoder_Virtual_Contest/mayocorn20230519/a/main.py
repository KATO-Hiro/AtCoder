# -*- coding: utf-8 -*-


from math import sqrt


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            ans.add(j)
            ans.add(n // j)

    for ans_i in sorted(ans):
        print(ans_i)


if __name__ == "__main__":
    main()
