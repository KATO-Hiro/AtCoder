# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 子どもが持っているアメの最小個数がx以上かどうかを二分探索で判定
    def f(x):
        count = 0

        for ai in a:
            count += max(0, ((x - ai + k - 1) // k))

        return count <= m

    ok = -1
    ng = 10**18

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj):
            ok = wj
        else:
            ng = wj

    remain = m

    # x個を配分し、残りの操作回数をx個ちょうどの子どもに配分
    hq = []

    for i, ai in enumerate(a):
        count = max(0, (ok - ai + k - 1) // k)
        heappush(hq, (ai + k * count, i))
        remain -= count

    for i in range(remain):
        ai, j = heappop(hq)
        heappush(hq, (ai + k, j))

    ans = [0] * n

    for ai, j in hq:
        ans[j] = ai

    print(*ans)


if __name__ == "__main__":
    main()
