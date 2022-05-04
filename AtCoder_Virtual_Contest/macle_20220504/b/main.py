# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    # https://blog.hamayanhamayan.com/entry/2017/11/11/224754
    # Key Insight: 確率の逆数が回数の期待値
    # 1回の試行に必要な時間 * 回数の期待値
    time = 1900 * m + 100 * (n - m)
    e = 2 ** m
    ans = time * e
    print(ans)


if __name__ == "__main__":
    main()
