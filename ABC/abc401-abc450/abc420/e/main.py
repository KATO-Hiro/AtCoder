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
        self.has_black = [set() for _ in range(number_count)]

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

        self.has_black[x] |= self.has_black[y]
        return True

    def update_color(self, number: int) -> None:
        root = self.find_root(number)

        if number in self.has_black[root]:
            self.has_black[root].discard(number)
        else:
            self.has_black[root].add(number)

    def is_reachable(self, number: int) -> bool:
        root = self.find_root(number)

        if len(self.has_black[root]) >= 1:
            return True

        return False


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(q):
        type, *args = list(map(int, input().split()))

        if type == 1:
            u, v = args
            u -= 1
            v -= 1

            uf.merge_if_needs(u, v)
        elif type == 2:
            v = args[0] - 1
            uf.update_color(v)
        else:
            v = args[0] - 1

            if uf.is_reachable(v):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
