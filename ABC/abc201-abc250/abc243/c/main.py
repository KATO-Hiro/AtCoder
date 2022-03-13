# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = list()
    d = defaultdict(list)

    for i in range(n):
        xi, yi = map(int, input().split())
        xy.append((xi, yi))

    s = input().rstrip()

    for i in range(n):
        xi, yi = xy[i]
        d[yi].append((xi, s[i]))
    
    for values in d.values():
        values = sorted(values)

        for (_, dir1), (_, dir2) in zip(values, values[1:]):
            if dir1 == "R" and dir2 == "L":
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
