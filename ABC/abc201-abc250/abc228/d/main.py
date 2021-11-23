# -*- coding: utf-8 -*-


class BalancingTree:
    """
    Self-balancing binary search tree using pivot values.
    `std::set` in C++.
    See:
    https://qiita.com/Kiri8128/items/6256f8559f0026485d90
    """

    def __init__(self, n):
        self.N = n
        self.root = self.node(1 << n, 1 << n)

    def append(self, v): # Note: v does not exist in the tree.
        v += 1
        nd = self.root

        while True:
            if v == nd.value:
                # v is already in the tree.
                # TODO: Write code here, if do something.
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)

                if mi < nd.pivot:
                    nd.value = ma

                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p) // 2)
                        break
                else:
                    nd.value = mi

                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p) // 2)
                        break

    def leftmost(self, nd):
        if nd.left: 
            return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: 
            return self.rightmost(nd.right)
        return nd

    def find_l(self, v):
        """The maximum value among the values truly less than v (If not, -1).
        """

        v += 1
        nd = self.root
        prev = 0

        if nd.value < v: 
            prev = nd.value

        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value

                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v):
        """The smallest value among the values truly greater than v 
        (if not, root).
        """

        v += 1
        nd = self.root
        prev = 0

        if nd.value > v: 
            prev = nd.value

        while True:
            if v < nd.value:
                prev = nd.value

                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1 << self.N) - 1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None):
        v += 1

        if not nd: 
            nd = self.root
        if not prev: 
            prev = nd

        while v != nd.value:
            prev = nd

            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    #####
                    return

        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)    
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []

            if nd.left:
                re += debug_node(nd.left)
            if nd.value: 
                re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re

        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []

            if nd.left:
                re += debug_node(nd.left)
            if nd.value: 
                re.append(nd.value - 1)
            if nd.right:
                re += debug_node(nd.right)
            return re
        return debug_node(self.root)[:-1]


def main():
    import sys

    input = sys.stdin.readline

    n = 2 ** 20
    q = int(input())
    a = [-1] * n
    bt = BalancingTree(21)
    inf = float('inf')

    for i in range(n + 1):
        bt.append(i)

    for _ in range(q):
        ti, xi = map(int, input().split())

        if ti == 1:
            h = xi
            h %= n
            index = inf

            if h in bt:
                index = h
            else:
                pos = bt.find_r(h)

                if pos == n:
                    index = bt.min
                else:
                    index = pos
            
            a[index] = xi
            bt.delete(index)
        else:
            print(a[xi % n])


if __name__ == "__main__":
    main()
