# -*- coding: utf-8 -*-


class UnionFind(object):
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


def main():
    from collections import Counter

    n, k, l = map(int, input().split())
    road = UnionFind(n)
    rail = UnionFind(n)

    for _ in range(k):
        pi, qi = map(lambda x: int(x) - 1, input().split())

        if road.is_same_group(pi, qi):
            continue

        road.merge_if_needs(pi, qi)

    for _ in range(l):
        ri, si = map(lambda x: int(x) - 1, input().split())

        if rail.is_same_group(ri, si):
            continue

        rail.merge_if_needs(ri, si)

    # See:
    # https://atcoder.jp/contests/arc065/submissions/3559412
    # http://tutuz.hateblo.jp/entry/2018/07/25/225115
    # http://baitop.hatenadiary.jp/entry/2018/06/26/224712
    pairs = Counter()
    ans = [0 for _ in range(n)]

    for i in range(n):
        hwy = road.find_root(i)
        rwy = rail.find_root(i)
        pairs[(hwy, rwy)] += 1

    for i in range(n):
        hwy = road.find_root(i)
        rwy = rail.find_root(i)
        ans[i] = pairs[(hwy, rwy)]

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
