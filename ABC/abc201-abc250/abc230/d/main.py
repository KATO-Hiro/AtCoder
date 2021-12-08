# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    walls = list()
    count = 0

    for i in range(n):
        li, ri = map(int, input().split())
        walls.append((ri, li))
    
    broken_point = -1
    
    for ri, li in sorted(walls):
        if li <= broken_point:
            continue

        count += 1
        broken_point = ri + d - 1

    print(count)


if __name__ == "__main__":
    main()
