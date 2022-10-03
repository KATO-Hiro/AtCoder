# -*- coding: utf-8 -*-


def f(a, wj):
    total = 0

    for ai in a:
        total += min(ai, wj)
    
    return total


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 円環を展開して、数列として考える
    # 周期性に着目
    # 1周ちょうど * m回 + 端数に分解
    # mを二分探索
    ok, ng = 0, 10 ** 12 + 1

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(a, wj) <= k:
            ok = wj
        else:
            ng = wj
    
    k -= f(a, ok)
    ans = [max(ai - ok, 0) for ai in a]

    for i, value in enumerate(ans):
        if k > 0 and value > 0:
            ans[i] -= 1
            k -= 1

    print(*ans)


if __name__ == "__main__":
    main()
