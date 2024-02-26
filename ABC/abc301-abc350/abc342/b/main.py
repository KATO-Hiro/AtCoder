# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        ai, bi = map(int, input().split())
        pos_ai, pos_bi = 0, 0

        for i, pi in enumerate(p):
            if pi == ai:
                pos_ai = i
            elif pi == bi:
                pos_bi = i

        if pos_ai < pos_bi:
            ans = ai
        elif pos_bi < pos_ai:
            ans = bi

        print(ans)


if __name__ == "__main__":
    main()
