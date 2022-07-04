# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = list(input().rstrip())
    count = 0

    for i in range(q):
        ti, xi = map(int, input().split())

        if ti == 1:
            count += xi
            count %= n
        else:
            xi -= 1
            index = n - count
            new_index = index + xi
            new_index %= n

            print(s[new_index])


if __name__ == "__main__":
    main()
