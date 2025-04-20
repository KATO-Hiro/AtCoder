# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(int)
    ans = m * (m - 1) // 2

    for _ in range(m):
        ai, bi = map(int, input().split())

        # 平行な線分の判定: (ai + bi) % nが等しい
        c = (ai + bi) % n
        d[c] += 1

    for k in d.values():
        ans -= k * (k - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
