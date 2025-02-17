# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = set()
    ans = 0

    for _ in range(m):
        ui, vi = map(int, input().split())

        if ui == vi or (ui, vi) in edges or (vi, ui) in edges:
            ans += 1
        else:
            edges.add((ui, vi))

    print(ans)


if __name__ == "__main__":
    main()
