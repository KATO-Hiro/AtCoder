# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappush, heappushpop

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    count = 0
    b = []

    for ai in a:
        while ai % 2 == 0:
            ai //= 2
            count += 1

        heappush(b, ai)

    # See:
    # https://atcoder.jp/contests/past202109-open/submissions/26383164
    for _ in range(count):
        heappushpop(b, b[0] * 3)

    print(b[0])


if __name__ == "__main__":
    main()
