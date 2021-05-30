# -*- coding: utf-8 -*-


from heapq import heapify, heappop, heappush


class Heapq:
    """
    Heapq()    : 本体qと削除用pの2本のheapqを用意する
    build(a)   : 配列aからプライオリティキューqを構築する
    push(x)    : プライオリティキューにxを追加
    erase(x)   : プライオリティーキューからxを(疑似的に)削除
    clean()    : 削除予定でトップに来た要素をq,pからpop
    pop((exc)) : トップの要素をqからpop (qが空の場合、excを返す)
    top((exc)) : トップの要素の値を取得  (qが空の場合、excを返す)

    See:
    https://qiita.com/physharp/items/f9229ab879cac9a944d7
    """

    def __init__(self):
        self.q = []
        self.p = []

    def build(self, a):
        self.q = a
        heapify(self.q)

    def push(self, x):
        heappush(self.q, x)

    def erase(self, x):
        heappush(self.p, x)
        self.clean()

    def clean(self):
        while self.p and self.q[0] == self.p[0]:
            heappop(self.q)
            heappop(self.p)

    def pop(self, exc=None):
        self.clean()
        if self.q:
            return heappop(self.q)
        return exc

    def top(self, exc=None):
        self.clean()
        if self.q:
            return self.q[0]
        return exc


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    g_count = 2 * 10 ** 5
    groups = [Heapq() for _ in range(g_count)]
    ab = list()

    for _ in range(n):
        ai, bi = map(int, input().split())
        bi -= 1
        ab += [[ai, bi]]

        groups[bi].push(-ai)

    equality = Heapq()

    # Get max value in each group.
    for group in groups:
        if group.q:
            equality.push(-group.top())

    ans = list()

    for _ in range(q):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1

        rating, group_id = ab[ci]

        # Remove rating in group_id and max value in group_id of equality.
        equality.erase(-groups[group_id].top())
        groups[group_id].erase(-rating)

        # Get max value in group ci and add equality.
        if groups[group_id].q:
            equality.push(-groups[group_id].top())

        # Update di from ci.
        ab[ci][1] = di

        # Remove max value in group_id of equality.
        if groups[di].q:
            di_max = -groups[di].top()
            equality.erase(di_max)

        # Get max value in group di and add equality.
        groups[di].push(-ab[ci][0])
        equality.push(-groups[di].top())

        ans += [equality.top()]

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
