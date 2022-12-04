# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline
    
    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    t = [input().rstrip() for _ in range(h)]
    d = defaultdict(int)
    e = defaultdict(int)

    for col in zip(*s):
        d[col] += 1

    for col in zip(*t):
        e[col] += 1
    
    if d == e:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
