# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    for i, g in enumerate(graph):
        if i == 0:
            continue

        si = ", ".join(map(str, g))
        print(f"{i}: {{{si}}}")


if __name__ == "__main__":
    main()
