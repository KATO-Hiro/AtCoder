# -*- coding: utf-8 -*-


def is_on_circle(xi, yi, ri, x, y):
    if (x - xi) ** 2 + (y - yi) ** 2 == ri**2:
        return True
    else:
        return False


from enum import Enum, auto


# See:
# https://docs.python.org/ja/3/howto/enum.html
class TwoCirclesPosition(Enum):
    Inside = auto()
    Inscribed = auto()
    Intersect = auto()
    Circumscribed = auto()
    Outside = auto()


# See:
# https://www.mathlion.jp/article/ar131.html
def is_intersected(xi: int, yi: int, ri: int, xj: int, yj: int, rj: int):
    dist = abs(xi - xj) ** 2 + abs(yi - yj) ** 2

    if rj > ri:
        ri, rj = rj, ri

    if (ri - rj) ** 2 > dist:
        return TwoCirclesPosition.Inside
    if (ri - rj) ** 2 == dist:
        return TwoCirclesPosition.Inscribed
    elif (ri - rj) ** 2 < dist < (ri + rj) ** 2:
        return TwoCirclesPosition.Intersect
    elif dist == (ri + rj) ** 2:
        return TwoCirclesPosition.Circumscribed
    elif dist > (ri + rj) ** 2:
        return TwoCirclesPosition.Outside


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
    """

    def __init__(self, number_count: int) -> None:
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

    def get_roots(self) -> List[int]:
        return [i for i, x in enumerate(self.parent_numbers) if x < 0]

    def get_edge_count(self, number: int) -> int:
        return self.edge_count[number]

    def get_group_count(self) -> int:
        return self.group_count


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [tuple(map(int, input().split())) for _ in range(n)]
    uf = UnionFind(n)

    # 円のペアが内接・交差・外接している = 同じ連結成分
    for i in range(n):
        xi, yi, ri = xyr[i]

        for j in range(i + 1, n):
            xj, yj, rj = xyr[j]
            result = is_intersected(xi, yi, ri, xj, yj, rj)

            if (
                result == TwoCirclesPosition.Inside
                or result == TwoCirclesPosition.Outside
            ):
                continue

            uf.merge_if_needs(i, j)

    # 始点・終点がどの円にあるか?
    s, t = list(), list()

    for i, (xi, yi, ri) in enumerate(xyr):
        if is_on_circle(xi, yi, ri, sx, sy):
            s.append(i)

        if is_on_circle(xi, yi, ri, tx, ty):
            t.append(i)

    # print(s, t)

    # 始点・終点のペアが同じ連結成分にあるか?
    for si in s:
        for tj in t:
            if uf.is_same_group(si, tj):
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
