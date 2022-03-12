# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = dict()

    for i in range(n):
        xi, yi = map(int, input().split())
        xi -= 1

        if yi not in d.keys():
            d[yi] = [(i, xi)]
        else:
            d[yi].append([i, xi])
    
    s = input().rstrip()

    for key, values in d.items():
        left = list()
        right = list()

        for i, pos in values:
            if s[i] == 'L':
                left.append(pos)
            else:
                right.append(pos)
        
        if len(left) == 0 or len(right) == 0:
            continue
        
        left = sorted(left)

        for r in right:
            index = bisect(left, r)

            if index != len(left):
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
