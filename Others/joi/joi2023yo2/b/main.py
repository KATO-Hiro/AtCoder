# -*- coding: utf-8 -*-


from bisect import bisect_left, bisect_right
from typing import List


def bisect_le(sorted_array: List[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    abcd = [sorted(list(map(int, input().split()))) for _ in range(4)]
    inf = 10**18
    ans = inf

    # クラスを固定して、代表eiを一人選ぶ
    # eijの身長hiが最大と仮定したとき、残りの3クラスはhi以下の最大値hjとなる代表を選ぶ
    for i, ei in enumerate(abcd):
        for eij in ei:
            members = [eij]

            for j in range(4):
                if i == j:
                    continue

                _, hj = bisect_le(abcd[j], eij)

                if hj is not None:
                    members.append(hj)

            if len(members) != 4:
                continue

            candidate = max(members) - min(members)
            ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
