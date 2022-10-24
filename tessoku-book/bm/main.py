# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    graph = [[] for _ in range(n)]
    
    for i, ai in enumerate(a, 1):
        ai -= 1
    
        graph[ai].append(i)
    
    dp = [0] * n

    for i in range(n - 1, -1, -1):
        for j in range(len(graph[i])):
            dp[i] += dp[graph[i][j]] + 1
    
    print(*dp)


if __name__ == "__main__":
    main()
