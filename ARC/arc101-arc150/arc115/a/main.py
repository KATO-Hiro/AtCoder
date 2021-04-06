# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    odd = 0
    even = 0

    for i in range(n):
        si = input().rstrip()
        count = si.count("1")

        if count % 2 == 0:
            even += 1
        else:
            odd += 1

    print(odd * even)


if __name__ == "__main__":
    main()
