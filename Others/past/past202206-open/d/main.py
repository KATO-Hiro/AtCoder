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


def get_offset(alphabet: str, base_alphabet: str = 'A') -> int:
    '''Get offset between the base_alphabet and alphabet.
    Args:
        alphabet: The alphabet to use. 
        base_alphabet: The base alphabet to use.
    Returns:
        difference between the base_alphabet and alphabet.
    
    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    '''   

    return ord(alphabet) - ord(base_alphabet)


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    uf = UnionFind(30)

    for i in range(n):
        ai, bi = input().rstrip().split()
        aj = get_offset(ai, 'a')
        bj = get_offset(bi, 'a')
        uf.merge_if_needs(aj, bj)

    s = input().rstrip()
    t = input().rstrip()

    for si, ti in zip(s, t):
        if si == ti:
            continue

        sj = get_offset(si, 'a')
        tj = get_offset(ti, 'a')

        if not uf.is_same_group(sj, tj):
            print("No")
            exit()
    
    print("Yes")



if __name__ == "__main__":
    main()
