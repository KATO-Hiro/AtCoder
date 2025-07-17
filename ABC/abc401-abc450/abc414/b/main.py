# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    total = 0
    ans = []

    for _ in range(n):
        ci, li = input().rstrip().split()
        li = int(li)

        if total + li > 100:
            print("Too Long")
            exit()

        total += li
        ans += [ci] * li

    print("".join(ans))


if __name__ == "__main__":
    main()
