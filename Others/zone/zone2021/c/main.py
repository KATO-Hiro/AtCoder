# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = 5
    abc = list()

    for i in range(n):
        alpha = list(map(int, input().split()))
        abc.append(alpha)

    # 答え(チームの総合力)を決め打って二分探索
    # 初期化
    ac = 0
    wa = 10 ** 9 + 1

    while (wa - ac) > 1:
        wj = (wa + ac) // 2
        patterns = set()

        # 各要素が、決め打った値以上か未満かを判定し、二進数に変換
        # 0 〜 1 << m - 1で管理
        for i in range(n):
            pattern = 0

            for j in range(m):
                if abc[i][j] >= wj:
                    pattern |= 1 << j

            patterns.add(pattern)

        ok = False

        # k <= j <= iの範囲で全探索
        for i, value_i in enumerate(patterns):
            for j, value_j in enumerate(patterns):
                for k, value_k in enumerate(patterns):
                    if k <= j <= i:
                        if value_i | value_j | value_k == ((1 << m) - 1):
                            ok = True

        if ok:
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == "__main__":
    main()
