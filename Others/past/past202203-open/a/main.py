# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    abc = list(map(int, input().split()))
    ans = list()

    for x, y in combinations(abc, 2):
        ans.append(x * y)
    
    print(min(ans), max(ans))


if __name__ == "__main__":
    main()
