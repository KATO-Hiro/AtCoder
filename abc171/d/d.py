# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    d = [0 for _ in range(10 ** 5)]
    ans = sum(a)

    for ai in a:
        d[ai - 1] += 1

    for i in range(q):
        bi, ci = map(int, input().split())

        bi_count = d[bi - 1]
        ans += (ci - bi) * bi_count
        print(ans)

        d[ci - 1] += d[bi - 1]
        d[bi - 1] = 0


if __name__ == '__main__':
    main()
