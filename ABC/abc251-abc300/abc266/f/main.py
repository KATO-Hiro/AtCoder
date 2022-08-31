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


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 8)

    n = int(input())
    graph = [[] for _ in range(n)]
    uv = list()
    
    for _ in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)

        uv.append((ai, bi))
    
    visited = [False] * n
    on_cycle = [False] * n
    no_cycle = -1
    
    # サイクルをdfsで検出
    def dfs(vertex, parent=-1):
        if visited[vertex]:
            return vertex
        
        visited[vertex] = True

        for to in graph[vertex]:
            if to == parent:
                continue

            r = dfs(to, vertex)

            if r == no_cycle:
                continue

            on_cycle[vertex] = True

            if r == vertex:
                return no_cycle

            return r
        
        return no_cycle

    dfs(0)
    
    uf = UnionFind(n)

    # サイクルの頂点を根とする木を構築
    for ui, vi in uv:
        if on_cycle[ui] and on_cycle[vi]:
            continue

        uf.merge_if_needs(ui, vi)
    
    q = int(input())
    ans = ["No"] * q

    # 同じ連結成分なら、単純パスが一意に定まる
    for i in range(q):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1

        if uf.is_same_group(xi, yi):
            ans[i] = "Yes"
    
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
