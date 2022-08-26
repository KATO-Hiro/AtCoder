# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    c = defaultdict(int)

    for i in range(1, n + 1):
        si = list(str(i))
        top = int(si[0])
        bottom = int(si[-1])
        c[(top, bottom)] += 1
    
    ans = 0

    for i in range(1, 10):
        for j in range(1, 10):
                ans += c[(i, j)] * c[(j, i)]
    
    print(ans)


if __name__ == "__main__":
    main()
