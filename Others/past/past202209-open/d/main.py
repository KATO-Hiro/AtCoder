# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = set()

    for _ in range(m):
        ui, vi = map(int, input().split())

        if ((ui, vi) in graph) or ((vi, ui) in graph):
            print("No")
            exit()
        elif (ui == vi):
            print("No")
            exit()
        elif ui > n or vi > n:
            print("No")
            exit()
        
        graph.add((ui, vi))

    print("Yes")
    

if __name__ == "__main__":
    main()
