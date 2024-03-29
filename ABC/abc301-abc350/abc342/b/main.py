# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        ai, bi = map(int, input().split())
        pos_ai, pos_bi = p.index(ai), p.index(bi)

        if pos_ai < pos_bi:
            ans = ai
        elif pos_bi < pos_ai:
            ans = bi

        print(ans)


if __name__ == "__main__":
    main()
