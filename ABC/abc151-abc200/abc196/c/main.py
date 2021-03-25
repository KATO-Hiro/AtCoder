# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for i in range(1, 10 ** 6 + 1):
        si = str(i) + str(i)
        j = int(si)

        if 1 <= j <= n:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
