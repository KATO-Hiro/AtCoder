# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    met = set()

    for a in range(2, 10**5 + 1):
        if a > n:
            break

        b = 2

        while a**b <= n:
            met.add(a**b)
            b += 1

    ans = n - len(met)
    print(ans)


if __name__ == "__main__":
    main()
