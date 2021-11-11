# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    n = int(input())
    b = [list(map(int, input().split())) for _ in range(n)]
    ans = list()
    master = [False] * n

    def dfs(m, ans):
        if not master[m]:
            master[m] = True
            ans.append(b[m][0])
        
        for aij in b[m][2:]:
            if master[aij - 1]:
                continue

            dfs(aij - 1, ans)
        
    dfs(n - 1, ans)
    print(sum(ans))


if __name__ == "__main__":
    main()
