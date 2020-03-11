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
    # 入力を高速化
    # See:
    # https://atcoder.jp/contests/iroha2019-day2/submissions/10220755
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    edge = [tuple(map(int, input().split() + [i])) for i in range(m)]

    # KeyInsight:
    # 連結な状態を保って、辺の本数を最小化すると木になる
    # 全域木: 無向グラフが与えられたときに、その部分グラフで任意の2頂点を連結にするような木
    # 最小全域木: 使われる辺のコストの和を最小にする全域木
    # この問題特有の部分: 水量(コスト)を最大にする
    # https://img.atcoder.jp/iroha2019-day2/editorial.pdf
    # 水量を降順に並び替える
    # 疑問点: なぜ貪欲的な方法でいいのか?
    # https://drken1215.hatenablog.com/entry/20121223/1356230697
    new_edge = sorted(edge, key=lambda x: x[2], reverse=True)
    uf = UnionFind(n)
    ans = [None for _ in range(n - 1)]
    count = 0

    for e in new_edge:
        x = e[0]
        y = e[1]
        index = e[3]

        # 同じグループかどうかを判定
        if uf.merge_if_needs(x - 1, y - 1):
            ans[count] = index + 1
            count += 1

    print('\n'.join(map(str, sorted(ans))))


if __name__ == '__main__':
    main()
