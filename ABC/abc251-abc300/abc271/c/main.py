# -*- coding: utf-8 -*-


def f(wj, a, n):
    # 連続する要素の長さを求める
    count = len(set(range(1, wj + 1)) & a)

    # そのまま読むことができる冊数 + 2冊売って買った冊数
    if count + (n - count) // 2 >= wj:
        return True
    else:
        return False


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = set(map(int, input().split()))  # 集合として扱う
    ok, ng = -1, 10 ** 6

    # 連続して本が読める = 単調性
    # 答えを決め打ちして二分探索
    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj, a, n):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
