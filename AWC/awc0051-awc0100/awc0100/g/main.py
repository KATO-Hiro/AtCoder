# -*- coding: utf-8 -*-


def main():
    import sys
    from atcoder.dsu import DSU

    input = sys.stdin.readline

    n, m = map(int, input().split())
    uf = DSU(n + 1)

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        uf.merge(ai, bi)

    q = int(input())

    for _ in range(q):
        si = int(input())
        si -= 1

        root = uf.leader(si)
        ans = uf.size(root)
        print(ans)


if __name__ == "__main__":
    main()
