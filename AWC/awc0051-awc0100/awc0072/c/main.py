# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = list(map(int, input().split()))
    count = [0] * (n + 1)

    for _ in range(q):
        li, ri = map(int, input().split())
        li -= 1
        count[li] += 1
        count[ri] -= 1

    acc = list(accumulate(count))
    ans = []

    for si, acc_i in zip(s, acc):
        diff = max(0, si - acc_i)
        ans.append(diff)

    print(*ans)


if __name__ == "__main__":
    main()
