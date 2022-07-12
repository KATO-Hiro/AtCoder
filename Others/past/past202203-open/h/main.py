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
        from collections import defaultdict
        self.parent_numbers = [-1 for _ in range(number_count)]
        self.d = defaultdict(list)

        for i in range(number_count):
            self.d[i].append(i)

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

            for yi in self.d[y]:
                self.d[x].append(yi)

            self.d[y] = list()
        else:
            self.parent_numbers[y] += self.parent_numbers[x]
            self.parent_numbers[x] = y

            for xi in self.d[x]:
                self.d[y].append(xi)

            self.d[x] = list()
        return True


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    uf = UnionFind(n + 10)

    for i in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            u, v = qi[1], qi[2]
            u -= 1
            v -= 1

            if not uf.is_same_group(u, v):
                uf.merge_if_needs(u, v)
        else:
            u = qi[1]
            u -= 1
            root = uf.find_root(u)
            vs = sorted(uf.d[root])
            ans = list()

            for vi in vs:
                ans.append(vi + 1)
            
            print(*ans)


if __name__ == "__main__":
    main()


