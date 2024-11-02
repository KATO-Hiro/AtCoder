# -*- coding: utf-8 -*-

from typing import List


class UnionFind:
    """Represents a data structure that tracks a set of elements partitioned
       into a number of disjoint (non-overlapping) subsets.

    Landau notation: O(α(n)), where α(n) is the inverse Ackermann function.

    See:
    https://www.youtube.com/watch?v=zV3Ul2pA2Fw
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    https://atcoder.jp/contests/abc120/submissions/4444942
    https://atcoder.jp/contests/abc292/submissions/39410075
    https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
    """

    def __init__(self, number_count: int) -> None:
        """
        Args:
            number_count: The size of elements (greater than 2).
        """
        self.number_count = number_count
        self.parent_numbers = [-1 for _ in range(number_count)]
        self.edge_count = [0 for _ in range(number_count)]
        self.group_count = number_count

    def find_root(self, number: int) -> int:
        """Follows the chain of parent pointers from number up the tree until
           it reaches a root element, whose parent is itself.
        Args:
            number: The trees id (0-index).

        Returns:
            The index of a root element.
        """
        if self.parent_numbers[number] < 0:
            return number

        self.parent_numbers[number] = self.find_root(self.parent_numbers[number])
        return self.parent_numbers[number]

    def merge_if_needs(self, number_x: int, number_y: int) -> bool:
        """Uses find_root to determine the roots of the tree number_x and
           number_y belong to. If the roots are distinct, the trees are combined
           by attaching the roots of one to the root of the other.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        """
        x = self.find_root(number_x)
        y = self.find_root(number_y)

        self.edge_count[x] += 1

        if x == y:
            return False

        self.group_count -= 1

        if self.parent_numbers[x] > self.parent_numbers[y]:
            x, y = y, x

        self.parent_numbers[x] += self.parent_numbers[y]
        self.parent_numbers[y] = x
        self.edge_count[x] += self.edge_count[y]
        return True

    def get_groups(self) -> List[List[int]]:
        roots: List[int] = [self.find_root(i) for i in range(self.number_count)]
        groups: List[List[int]] = [[] for _ in range(self.number_count)]

        for i in range(self.number_count):
            groups[roots[i]].append(i)

        return list(filter(lambda g: g, groups))


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    degrees = [0] * n
    uv = list()

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        uv.append((ai, bi))

        degrees[ai] += 1
        degrees[bi] += 1

    # 次数3の頂点のうち、隣接しているものを同じ連結成分にまとめる
    uf = UnionFind(n)
    # 次数3 - 次数2の辺の数 (次数3の頂点に隣接している次数2の頂点を走査するため、添え字は次数3の頂点番号)
    counts = [0] * n

    for ui, vi in uv:
        if degrees[ui] == 3 and degrees[vi] == 3:
            uf.merge_if_needs(ui, vi)
        elif degrees[ui] == 3 and degrees[vi] == 2:
            counts[ui] += 1
        elif degrees[ui] == 2 and degrees[vi] == 3:
            counts[vi] += 1

    ans = 0

    # 同じ連結成分を対象として、次数3の頂点に隣接している次数2の頂点のペアを求める
    for group in uf.get_groups():
        count = 0

        for vertex in group:
            count += counts[vertex]

        ans += count * (count - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
