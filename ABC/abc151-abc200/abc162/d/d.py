# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()

    # KeyInsight
    # 条件を満たす場合を直接求めるのが難しい場合は、補集合を考える

    # R, G, Bは、それぞれ独立に扱える
    r_count = s.count('R')
    g_count = s.count('G')
    b_count = s.count('B')

    ans = r_count * g_count * b_count

    # i, jを固定して全探索
    # 常にi < jとなるように添字を振るのもポイント
    for j in range(n):
        for i in range(j):
            # kは、i, jから計算
            k = 2 * j - i

            # インデックスエラーを回避
            if k < n:
                if s[i] == s[j]:
                    continue
                elif s[i] == s[k]:
                    continue
                elif s[j] == s[k]:
                    continue

                ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
