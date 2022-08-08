# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    d = defaultdict(int)

    for i, pi in enumerate(p, 2):
        d[i] = pi
    
    def dfs(i, ans):
        if i == 1:
            print(ans)
            exit()
        
        dfs(d[i], ans + 1)
    
    dfs(d[n], 1)


if __name__ == "__main__":
    main()
