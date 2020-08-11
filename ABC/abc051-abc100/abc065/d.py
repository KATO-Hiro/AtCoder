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
    import sys
    input = sys.stdin.readline

    n = int(input())
    x = [None for _ in range(n)]
    y = [None for _ in range(n)]

    for i in range(n):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1

        x[i] = (xi, i)
        y[i] = (yi, i)

    # 最小全域木: 無向グラフで、任意の頂点のペアが行き来できる&そのときのコストを最小にしたい
    # x, y座標を別々に考える
    new_x = sorted(x)
    new_y = sorted(y)
    road = list()

    # x, y座標ともに最も近い点のペアを選択する(それ以外の点のペアを選んでもコストは増えるだけ)
    # 計算量がO(N^2)からO(N)に落とせる
    for _from, _to in zip(new_x, new_x[1:]):
        cost = abs(_from[0] - _to[0])
        road.append((_from[1], _to[1], cost))

    for _from, _to in zip(new_y, new_y[1:]):
        cost = abs(_from[0] - _to[0])
        road.append((_from[1], _to[1], cost))

    # コストが最小のものから選ぶ
    new_road = sorted(road, key=lambda x: x[2])
    uf = UnionFind(n)
    ans = 0

    # 同じグループに存在するかをチェックして、コストを加算
    for nr in new_road:
        if uf.merge_if_needs(nr[0], nr[1]):
            ans += nr[2]

    print(ans)


if __name__ == '__main__':
    main()
