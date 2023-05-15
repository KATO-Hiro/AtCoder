# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    d = int(input())
    # 降順 + 累積和
    n = sorted(map(int, list(input().rstrip())), reverse=True)
    a = [0] + list(accumulate(n))
    ans = 0

    for i in range(d):
        m = d - i - 1
        ai = n[i]
        ans += ai * m - (a[d] - a[i + 1])

    print(ans)


if __name__ == "__main__":
    main()
