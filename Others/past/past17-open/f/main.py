# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    s = list(input().rstrip().split())
    mod = 998244353
    graph = [[] for _ in range(n)]

    for i, pi in enumerate(p, 1):
        pi -= 1
        graph[pi].append(i)

    # See:
    # https://atcoder.jp/contests/past17-open/submissions/53272179
    def dfs(i):
        if s[i] == "+":
            a, b = graph[i]
            result = (dfs(a) + dfs(b)) % mod
        elif s[i] == "x":
            a, b = graph[i]
            result = (dfs(a) * dfs(b)) % mod
        else:
            result = int(s[i])

        return result

    print(dfs(0))


if __name__ == "__main__":
    main()
