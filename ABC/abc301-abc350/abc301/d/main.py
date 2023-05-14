# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()[::-1]
    m = len(s)
    n = int(input())
    ans = 0

    # See:
    # https://atcoder.jp/contests/abc301/submissions/41312127
    # 先頭の桁からGreedyに見る
    # ?を0で埋める = '1'の部分を加算
    for i in range(m):
        if s[i] == "1":
            ans |= 1 << i

    if ans > n:
        print(-1)
        exit()

    # ?を1で埋めたときにn以下か?
    for i in reversed(range(m)):
        if s[i] == "?" and (ans | 1 << i) <= n:
            ans |= 1 << i

    print(ans)


if __name__ == "__main__":
    main()
