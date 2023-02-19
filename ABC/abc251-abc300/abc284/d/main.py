# -*- coding: utf-8 -*-


def solve():
    from math import sqrt

    n = int(input())
    a = 1

    while True:
        a += 1

        if n % a != 0:
            continue

        n //= a

        if n % a == 0:
            print(a, n // a)
            break
        else:
            print(int(sqrt(n)), a)
            break


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()
    

if __name__ == "__main__":
    main()
