# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0
    a = 1

    while a ** 3 <= n:
        b = a

        while a * (b ** 2) <= n:
            c = n // (a * b) - b + 1
            ans += c

            b += 1
        
        a += 1

    print(ans)


if __name__ == "__main__":
    main()
