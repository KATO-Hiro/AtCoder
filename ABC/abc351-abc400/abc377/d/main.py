# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    l_max = defaultdict(int)

    # rを固定したときに、最も右側のlにのみ関心がある
    # 差分を更新: r + 1のときに、最も右側のlの位置を求める
    for _ in range(n):
        li, ri = map(int, input().split())
        l_max[ri] = max(l_max[ri], li)

    l = 1
    ans = 0

    for r in range(1, m + 1):
        while l <= l_max[r]:
            l += 1

        ans += r - l + 1

    print(ans)


if __name__ == "__main__":
    main()
