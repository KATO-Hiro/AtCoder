# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    s = input().rstrip()
    d = defaultdict(list)

    for si, (xi, yi) in zip(s, xy):
        d[yi].append((xi, si))

    for key in d.keys():
        d[key].sort()

    for values in d.values():
        for (_, dir1), (_, dir2) in zip(values, values[1:]):
            if dir1 == "R" and dir2 == "L":
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
