# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    m = len(s)
    n = int(input())
    ans = 0

    # 先頭の桁からGreedyに見る
    for d in range(m):
        if s[d] == "1":
            ans += 1 << (m - d - 1)
        elif s[d] == "?":
            # "?"を1で仮置き
            ans += 1 << (m - d - 1)
            tmp = ans

            # d + 1桁以降の?を0で埋めたときにN以下か?
            # = 1の桁だけ見る
            for i in range(d + 1, m):
                if s[i] == "1":
                    tmp += 1 << (m - i - 1)

            # 条件を満たさないときは"0"を置く
            if tmp > n:
                ans -= 1 << (m - d - 1)

    if ans > n:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
