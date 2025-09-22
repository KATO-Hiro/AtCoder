# -*- coding: utf-8 -*-


def main():
    import sys

    from collections import deque, defaultdict
    from atcoder.dsu import DSU

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(set)

    for i in range(n):
        ai, bi = map(int, input().split())

        d[ai].add(i + 1)
        d[bi].add(i + 1)

    q = deque([0])
    used = set()
    dsu = DSU(n + 1)

    while q:
        cur = q.popleft()

        if cur in used:
            continue

        used.add(cur)

        for to in d[cur]:
            dsu.merge(cur, to)

            if to in used:
                continue

            q.append(to)

    ans = dsu.size(dsu.leader(0)) - 1
    print(ans)


if __name__ == "__main__":
    main()
