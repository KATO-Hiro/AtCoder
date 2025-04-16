# -*- coding: utf-8 -*-

from typing import List


def run_length_encoding(iterable: list) -> List[list]:
    """
    Args:
        iterable: A list of numbers or strings.

    Returns:
        A list containing consecutive characters and their count.

    See:
    https://qiita.com/DaikiSuyama/items/07e237b7372e7c7b3432
    """

    from itertools import groupby

    results = [[key, len(list(group))] for key, group in groupby(iterable)]

    return results


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = list(input().rstrip())

    # 前処理: o が連続しない => o の両隣は . と言い換え
    for i, si in enumerate(s):
        if si == "o":
            if i - 1 >= 0:
                s[i - 1] = "."
            if i + 1 < n:
                s[i + 1] = "."

    # o.???.o.?????のような構造
    # o の数を数えて、残りを?に割り当てる
    remain = k - s.count("o")

    # ??? の区間と取りうる最大の o の個数を求める
    results = run_length_encoding(s)
    total = 0
    ps = list()

    for key, count in results:
        if key == "?":
            ps.append((total, total + count))  # [left, right)

        total += count

    candidate_max = 0

    for left, right in ps:
        candidate_max += (right - left + 1) // 2

    # 場合分け
    # 1. o が 既に k 個使われている: ? を 全て . に置き換え
    if remain == 0:
        for i, si in enumerate(s):
            if si == "?":
                s[i] = "."
    # 2. ???に埋められる上限まで必要
    # 2.1 偶奇で場合分け: 偶数の場合は ?、奇数の場合は o.o.oで埋める
    elif remain == candidate_max:
        for left, right in ps:
            if (right - left) % 2 == 0:
                continue

            for i in range(right - left):
                if i % 2 == 0:
                    s[left + i] = "o"
                else:
                    s[left + i] = "."
    # 3. それ以外
    else:
        pass

    print("".join(s))


if __name__ == "__main__":
    main()
