# -*- coding: utf-8 -*-


class UnionFind:
    '''Represents a data structure that tracks a set of elements partitioned
       into a number of disjoint (non-overlapping) subsets.
    Landau notation: O(α(n)), where α(n) is the inverse Ackermann function.
    See:
    https://www.youtube.com/watch?v=zV3Ul2pA2Fw
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    https://atcoder.jp/contests/abc120/submissions/4444942
    https://www.youtube.com/watch?v=N_Xtv_mctTw
    https://atcoder.jp/contests/abc183/submissions/18111510
    '''

    def __init__(self, number_count: int):
        '''
        Args:
            number_count: The size of elements (greater than 2).
        '''
        from collections import defaultdict 

        self.parent_numbers = [-1 for _ in range(number_count)]
        self.group_ids = [defaultdict(int) for _ in range(number_count)]

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
        
        # x > y
        if self.parent_numbers[x] > self.parent_numbers[y]:
            x, y = y, x # swap
        
        for key, value in self.group_ids[y].items():
            self.group_ids[x][key] += value

        self.parent_numbers[x] += self.parent_numbers[y]
        self.parent_numbers[y] = x

        return True


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    uf = UnionFind(n)

    for i, ci in enumerate(c):
        uf.group_ids[i][ci - 1] += 1

    for i in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            ai, bi = qi[1], qi[2]
            ai -= 1
            bi -= 1

            if not uf.is_same_group(ai , bi):
                uf.merge_if_needs(ai, bi)
        else:
            xi, yi = qi[1], qi[2]
            xi -= 1
            yi -= 1
            root = uf.find_root(xi)

            print(uf.group_ids[root][yi])


if __name__ == "__main__":
    main()
