# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    size_max = 0
    ans = 1
    
    for i, g in enumerate(graph, 1):
        size = len(g)

        if size > size_max:
            size_max = size
            ans = i

    print(ans)
    

if __name__ == "__main__":
    main()
