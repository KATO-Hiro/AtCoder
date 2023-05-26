# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    ans = list()

    for b in range(1, x + 1):
        for p in range(2, 10 + 1):
            if b**p <= x:
                ans.append(b**p)

    print(max(ans))


if __name__ == "__main__":
    main()
