# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    d = defaultdict(int)

    # 人iが喜ぶ料理の移動回数に着目
    for i, pi in enumerate(p):
        j = (pi - i - 1) % n

        for k in range(3):
            d[(j + k) % n] += 1
    
    print(max(d.values()))


if __name__ == "__main__":
    main()
