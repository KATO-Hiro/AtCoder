# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    lr = sorted(
        [tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1]
    )
    # print(lr)
    x = -(10**18)
    ans = 0

    # 区間スケジューリング問題の応用
    for li, ri in lr:
        if x + d - 1 < li:
            x = ri
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
