# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(accumulate([0] + a))
    ans = 0

    # 最初だけ愚直に
    for i in range(1, m + 1):
        ans += i * a[i - 1]
    
    pre = ans
    
    # 差分を計算
    for i in range(m, n):
        candidate = pre
        candidate -= c[i] - c[i - m]
        candidate += m * a[i]
        ans = max(ans, candidate)
        pre = candidate

    print(ans)


if __name__ == "__main__":
    main()
