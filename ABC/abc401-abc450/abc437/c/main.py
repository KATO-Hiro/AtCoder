# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    wp = []
    sum_p = 0

    for _ in range(n):
        wi, pi = map(int, input().split())
        wp += [wi + pi]
        sum_p += pi

    wp.sort()

    for i in range(n):
        sum_p -= wp[i]

        if sum_p < 0:
            print(i)
            return


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
