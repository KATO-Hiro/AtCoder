# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    graph = [[False] * n for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai][bi] = True
        graph[bi][ai] = True
    
    ans = 0

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if not graph[a][b] and not graph[b][a]:
                    continue
                if not graph[b][c] and not graph[c][b]:
                    continue
                if not graph[c][a] and not graph[a][c]:
                    continue

                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
