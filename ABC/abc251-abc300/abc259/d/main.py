# -*- coding: utf-8 -*-


class UnionFind:
    '''Represents a data structure that tracks a set of elements partitioned
       into a number of disjoint (non-overlapping) subsets.
    Landau notation: O(α(n)), where α(n) is the inverse Ackermann function.
    See:
    https://www.youtube.com/watch?v=zV3Ul2pA2Fw
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    https://atcoder.jp/contests/abc120/submissions/4444942
    '''

    def __init__(self, number_count: int):
        '''
        Args:
            number_count: The size of elements (greater than 2).
        '''
        self.parent_numbers = [-1 for _ in range(number_count)]

    def find_root(self, number: int) -> int:
        '''Follows the chain of parent pointers from number up the tree until
           it reaches a root element, whose parent is itself.
        Args:
            number: The trees id (0-index).
        Returns:
            The index of a root element.
        '''
        if self.parent_numbers[number] < 0:
            return number

        self.parent_numbers[number] = self.find_root(self.parent_numbers[number])
        return self.parent_numbers[number]

    def get_group_size(self, number: int) -> int:
        '''
        Args:
            number: The trees id (0-index).
        Returns:
            The size of group.
        '''
        return -self.parent_numbers[self.find_root(number)]

    def is_same_group(self, number_x: int, number_y: int) -> bool:
        '''Represents the roots of tree number_x and number_y are in the same
           group.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        '''
        return self.find_root(number_x) == self.find_root(number_y)

    def merge_if_needs(self, number_x: int, number_y: int) -> bool:
        '''Uses find_root to determine the roots of the tree number_x and
           number_y belong to. If the roots are distinct, the trees are combined
           by attaching the roots of one to the root of the other.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        '''
        x = self.find_root(number_x)
        y = self.find_root(number_y)

        if x == y:
            return False

        if self.get_group_size(x) >= self.get_group_size(y):
            self.parent_numbers[x] += self.parent_numbers[y]
            self.parent_numbers[y] = x
        else:
            self.parent_numbers[y] += self.parent_numbers[x]
            self.parent_numbers[x] = y
        return True


def is_on_circle(xi, yi, ri, x, y):
    if (x - xi) ** 2 + (y - yi) ** 2 == ri ** 2:
        return True
    else:
        return False


def is_hit(xi, yi, ri, xj, yj, rj):
    dist = abs(xi - xj) ** 2 + abs(yi - yj) ** 2

    if (max(ri, rj) - min(ri, rj)) ** 2 <= dist <= (ri + rj) ** 2:
        return True
    else:
        return False


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [tuple(map(int, input().split())) for _ in range(n)]
    cs, ct = -1, -1 # s, tがどの円に属するか
    uf = UnionFind(n)

    # 始点・終点がどの円に属するか判定
    for i in range(n):
        xi, yi, ri = xyr[i]

        if is_on_circle(xi, yi, ri, sx, sy):
            cs = i
        if is_on_circle(xi, yi, ri, tx, ty):
            ct = i
    
    # 円同士が接するか判定
    for i in range(n):
        xi, yi, ri = xyr[i]

        for j in range(i + 1, n):
            xj, yj, rj = xyr[j]

            if is_hit(xi, yi, ri, xj, yj, rj):
                uf.merge_if_needs(i, j)
    
    if uf.is_same_group(cs, ct):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
