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
    
    for key, value in d.items():
        if key not in e.keys():
            print("No")
            exit()
        
        if e[key] != value:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
