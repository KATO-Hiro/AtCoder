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
    """

    def __init__(self, number_count: int):
        """
        Args:
            number_count: The size of elements (greater than 2).
        """
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

    def get_roots(self):
        return [i for i, x in enumerate(self.parent_numbers) if x < 0]

    def get_edge_count(self, number: int) -> int:
        return self.edge_count[number]

    def get_group_count(self) -> int:
        return self.group_count


def main():
    import sys
    from copy import deepcopy

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    wall_count = 0
    uf = UnionFind(h * w)

    # .をグラフ理論の連結成分とみなす
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                wall_count += 1
                continue

            base = w * i + j

            if (i + 1 < h) and s[i + 1][j] == ".":
                k = w * (i + 1) + j
                uf.merge_if_needs(base, k)

            if (j + 1 < w) and s[i][j + 1] == ".":
                k = w * i + (j + 1)
                uf.merge_if_needs(base, k)

    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    ans = 0

    # 壁のマスを一つ変更して、連結成分を(壁の個数 - 1) + (壁でないマスの集合 = 1)にできるか?
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                continue

            # ベースとなる結果からコピー
            uf2 = deepcopy(uf)
            base = w * i + j

            for dx, dy in dxy:
                ni = dy + i
                nj = dx + j

                if not (0 <= nj < w):
                    continue
                if not (0 <= ni < h):
                    continue
                if s[ni][nj] == "#":
                    continue

                k = w * ni + nj
                uf2.merge_if_needs(base, k)

            # print(i, j, uf2.get_group_count(), uf2.get_roots())

            if uf2.get_group_count() == wall_count:
                ans += 1

    # print(uf.get_group_count())
    # print(wall_count)
    print(ans)


if __name__ == "__main__":
    main()
