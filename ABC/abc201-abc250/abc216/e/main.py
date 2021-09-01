# -*- coding: utf-8 -*-


def f(k, a, x):
    count = 0

    for ai in a:
        count += max(ai - x, 0)
    
    return count <= k


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ng = -1
    ok = 2 * 10 ** 9 + 1

    while ok - ng > 1:
        mid = (ok + ng) // 2

        if f(k, a, mid):
            ok = mid
        else:
            ng = mid
    
    summed = 0
    ans = 0

    for ai in a:
        count = max(0, ai - ok)

        if count > 0:
            ans += (ai * (ai + 1) // 2) - (ok * (ok + 1) // 2)
            summed += count
    
    ans += (k - summed) * ok

    print(ans)


if __name__ == "__main__":
    main()
