# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [0 for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        if ai > bi:
            graph[ai] += 1
        if bi > ai:
            graph[bi] += 1
    
    print(sum([1 for g in graph if g == 1]))


if __name__ == "__main__":
    main()
