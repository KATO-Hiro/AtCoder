# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph_t = [[False] * n for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph_t[ai][bi] = True
        graph_t[bi][ai] = True

    graph_a = [[False] * n for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph_a[ai][bi] = True
        graph_a[bi][ai] = True
    
    for p in permutations(range(n)):
        ok = True

        for i in range(n):
            for j in range(n):
                if graph_t[i][j] != graph_a[p[i]][p[j]]:
                    ok = False
                    break
        
        if ok:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
