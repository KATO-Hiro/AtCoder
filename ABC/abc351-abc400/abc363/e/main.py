# -*- coding: utf-8 -*-


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

    def get_group_size(self, number: int) -> int:
        """
        Args:
            number: The trees id (0-index).

        Returns:
            The size of group.
        """
        return -self.parent_numbers[self.find_root(number)]

    def is_same_group(self, number_x: int, number_y: int) -> bool:
        """Represents the roots of tree number_x and number_y are in the same
           group.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        """
        return self.find_root(number_x) == self.find_root(number_y)

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


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, y = map(int, input().split())
    pos = defaultdict(list)

    for i in range(h):
        ai = list(map(int, input().split()))

        for j, aij in enumerate(ai):
            if aij <= y:
                # 0年スタートに
                pos[aij - 1].append((i, j))

    under_sea = [[False for _ in range(w)] for _ in range(h)]
    size = h * w
    # 海を超頂点として持つ
    uf = UnionFind(size + 1)
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    for year in range(y):
        for i, j in pos[year]:
            under_sea[i][j] = True
            v = i * w + j

            for dx, dy in dxy:
                ni = i + dy
                nj = j + dx

                # 海かどうかの判定
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    uf.merge_if_needs(size, v)
                else:
                    if not under_sea[ni][nj]:
                        continue

                    # 既に沈んでいる
                    uf.merge_if_needs(v, ni * w + nj)

        count = h * w - (uf.get_group_size(size) - 1)
        print(count)


if __name__ == "__main__":
    main()
