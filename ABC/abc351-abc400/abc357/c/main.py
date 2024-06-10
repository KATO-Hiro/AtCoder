# -*- coding: utf-8 -*-


def f(grid):
    results = []
    size = len(grid)

    for g in grid:
        results.append(g * 3)

    for g in grid:
        results.append(g + ["."] * size + g)

    for g in grid:
        results.append(g * 3)

    return results


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [["#"]]

    for _ in range(n):
        s = f(s)

    for si in s:
        print("".join(si))


if __name__ == "__main__":
    main()
