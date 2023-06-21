# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a, b, c = map(int, input().split())
    ans = 10**4
    count_max = 10**4

    for x in range(count_max):
        for y in range(count_max):
            d = a * x + b * y

            if d > n:
                break

            if (n - d) % c == 0:
                z = (n - d) // c

                ans = min(ans, x + y + z)

    print(ans)


if __name__ == "__main__":
    main()
