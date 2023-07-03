# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = [abs(ai) for ai in a]
    ans = sum(b)
    minus_count = sum([1 for ai in a if ai < 0])

    # 負の数を偶奇で場合分け
    # 偶数: 全て正の数にできそう?
    # 奇数: 絶対値が最小のもののみ負、それ以外は正?
    if minus_count % 2 == 1:
        ans -= min(b) * 2

    print(ans)


if __name__ == "__main__":
    main()
