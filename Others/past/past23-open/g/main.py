# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    acc = list(accumulate(a, initial=0))

    for _ in range(q):
        li, ri = map(int, input().split())
        li -= 1

        p1, q1 = divmod(ri, n)
        p2, q2 = divmod(li, n)

        ans = acc[n] * (p1 - p2) + acc[q1] - acc[q2]
        print(ans)


if __name__ == "__main__":
    main()
