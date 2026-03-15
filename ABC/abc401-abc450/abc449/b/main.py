# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, q = map(int, input().split())

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            r = query[1]
            print(w * r)
            h -= r
        else:
            c = query[1]
            print(h * c)
            w -= c


if __name__ == "__main__":
    main()
