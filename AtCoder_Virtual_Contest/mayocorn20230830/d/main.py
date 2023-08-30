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

    # 操作は直立したグループ('0')ごとに対して行うのが良い
    # 同じ状態をランレングス圧縮でまとめる
    results = run_length_encoding(s)
    # print(results)

    # 問題の言い換え
    # 連続した区間に'0'グループがk個以下含まれるときの最大の長さを求める
    # 尺取り法
    left, zero_count, size = 0, 0, 0
    ans = 0

    for right, (state, count) in enumerate(results):
        size += count

        if state == "0":
            zero_count += 1

        while zero_count > k:
            prev_state, prev_count = results[left]
            size -= prev_count

            if prev_state == "0":
                zero_count -= 1

            left += 1

        ans = max(ans, size)

    print(ans)


if __name__ == "__main__":
    main()
