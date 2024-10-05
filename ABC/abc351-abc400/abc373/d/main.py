# -*- coding: utf-8 -*-


class WeightedUnionFind:
    """Represents a data structure that tracks a set of elements partitioned
       into a number of disjoint (non-overlapping) subsets.
    Landau notation: O(α(n)), where α(n) is the inverse Ackermann function.

    See:
    https://www.youtube.com/watch?v=zV3Ul2pA2Fw
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    https://atcoder.jp/contests/abc120/submissions/4444942
    https://qiita.com/drken/items/cce6fc5c579051e64fab
    """

    def __init__(self, number_count: int):
        """
        Args:
            number_count: The size of elements (greater than 2).
        """
        self.parent_numbers = [i for i in range(number_count)]
        self.rank = [0 for _ in range(number_count)]
        self.diff_weight = [0 for _ in range(number_count)]

    def find_root(self, number: int) -> int:
        """Follows the chain of parent pointers from number up the tree until
           it reaches a root element, whose parent is itself.
        Args:
            number: The trees id (0-index).
        Returns:
            The index of a root element.
        """
        if self.parent_numbers[number] == number:
            return number
        else:
            parent_number = self.parent_numbers[number]
            root = self.find_root(parent_number)
            self.diff_weight[number] += self.diff_weight[parent_number]
            self.parent_numbers[number] = root
            return root

    def calc_weight(self, number: int) -> int:
        """Calculate the weight of the node.
        Args:
            number: The trees id (0-index).
        Returns:
            The weight of the node.
        """
        self.find_root(number)
        return self.diff_weight[number]

    def is_same_group(self, number_x: int, number_y: int) -> bool:
        """Represents the roots of tree number_x and number_y are in the same
           group.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        """
        return self.find_root(number_x) == self.find_root(number_y)

    def merge_if_needs(self, number_x: int, number_y: int, weight: int) -> bool:
        """Uses find_root to determine the roots of the tree number_x and
           number_y belong to. If the roots are distinct, the trees are
           combined by attaching the roots of one to the root of the other.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
            weight  : Cost between nodes.
        """
        # Correct the difference between the weight of root and number_x,
        # number_y.
        weight += self.calc_weight(number_x)
        weight -= self.calc_weight(number_y)
        root_x, root_y = self.find_root(number_x), self.find_root(number_y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
            weight = -weight
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.parent_numbers[root_y] = root_x
        self.diff_weight[root_y] = weight
        return True

    def calc_cost(self, from_x: int, to_y: int) -> int:
        """Calculate cost between nodes.
        Args:
            from_x: The trees x (0-index).
            to_y  : The trees y (0-index).
        Returns:
            Cost between nodes.
        """
        return self.calc_weight(to_y) - self.calc_weight(from_x)


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    uf = WeightedUnionFind(n)

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        uf.merge_if_needs(ai, bi, ci)

    for i in range(n):
        print(uf.calc_weight(i))


if __name__ == "__main__":
    main()
