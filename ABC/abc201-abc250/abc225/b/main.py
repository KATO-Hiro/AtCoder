# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    for g in graph:
        if len(g) == n - 1:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
