# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = [i for i in range(1, n + 1)]
    rotate_count = 0

    for _ in range(q):
        type, *query = map(int, input().split())

        if type == 1:
            p, x = query
            p -= 1
            a[(p + rotate_count) % n] = x
        elif type == 2:
            p = query[0] - 1
            print(a[(p + rotate_count) % n])
        else:
            k = query[0]
            rotate_count += k
            rotate_count %= n


if __name__ == "__main__":
    main()
