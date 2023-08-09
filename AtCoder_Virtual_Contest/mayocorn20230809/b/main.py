# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    ans = set()
    ans.add(1)

    for b in range(2, 40):
        p = 2

        while b**p <= x:
            ans.add(b**p)
            p += 1

    print(max(ans))


if __name__ == "__main__":
    main()
