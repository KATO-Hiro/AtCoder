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

        if x == y:
            return False

        if self.parent_numbers[x] > self.parent_numbers[y]:
            x, y = y, x

        self.parent_numbers[x] += self.parent_numbers[y]
        self.parent_numbers[y] = x
        return True

    def get_roots(self) -> List[int]:
        return [i for i, x in enumerate(self.parent_numbers) if x < 0]


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    uf = UnionFind(n)
    extras = []

    for i in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        if uf.is_same_group(ai, bi):
            extras.append((i, ai, bi))
        else:
            uf.merge_if_needs(ai, bi)

    roots = uf.get_roots()
    count = len(roots) - 1
    roots = set(roots)
    print(count)

    while len(roots) > 1:
        i, ai, bi = extras.pop()

        v = uf.find_root(ai)
        roots.discard(v)
        u = roots.pop()

        # つなぎ直した連結成分をrootsに追加
        uf.merge_if_needs(u, v)
        roots.add(uf.find_root(u))

        print(i + 1, ai + 1, u + 1)


if __name__ == "__main__":
    main()
