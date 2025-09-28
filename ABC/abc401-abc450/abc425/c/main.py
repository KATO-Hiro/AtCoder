# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(accumulate(a + a, initial=0))
    count = 0

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            count += query[1]
            count %= n
        else:
            l, r = query[1:]
            nl, nr = l + count - 1, r + count
            print(b[nr] - b[nl])


if __name__ == "__main__":
    main()
