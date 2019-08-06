# -*- coding: utf-8 -*-


class UnionFind(object):

    def __init__(self, number_count: int):
        self.parent_numbers = [-1 for _ in range(number_count)]

    def find_root(self, number: int) -> int:
        if self.parent_numbers[number] < 0:
            return number

        self.parent_numbers[number] = self.find_root(self.parent_numbers[number])
        return self.parent_numbers[number]

    def get_group_size(self, number: int) -> int:
        return -self.parent_numbers[self.find_root(number)]

    def is_same_group(self, number_x: int, number_y: int) -> bool:
        return self.find_root(number_x) == self.find_root(number_y)

    def merge_if_needs(self, number_x: int, number_y: int) -> bool:
        x = self.find_root(number_x)
        y = self.find_root(number_y)

        if x == y:
            return False

        if self.get_group_size(x) > self.get_group_size(y):
            self.parent_numbers[x] += self.parent_numbers[y]
            self.parent_numbers[y] = x
        else:
            # swap
            self.parent_numbers[y] += self.parent_numbers[x]
            self.parent_numbers[x] = y
        return True


def main():
    n, m = map(int, input().split())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    ans = [0 for _ in range(m)]
    ans[-1] = n * (n - 1) // 2
    uf = UnionFind(n)

    for i in range(m - 1, 0, -1):
        ans[i - 1] = ans[i]
        ai = ab[i][0]
        bi = ab[i][1]

        if not uf.is_same_group(ai, bi):
            ans[i - 1] -= uf.get_group_size(ai) * uf.get_group_size(bi)
            uf.merge_if_needs(ai, bi)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
