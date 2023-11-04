# -*- coding: utf-8 -*-


def main():
    import sys
    from typing import List, Tuple

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    no_color, black, white = 0, 1, -1
    colors = [no_color] * n

    for ai, bi in zip(a, b):
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    # See:
    # https://prd-xxx.hateblo.jp/entry/2017/10/13/004256
    def is_bipartite(
        start_id: int,
        graph: List[List],
        colors: List[int],
        black_count: int = 0,
        white_count: int = 0,
    ) -> Tuple[bool, int, int]:
        stack = [(start_id, black)]  # vertex, color

        while stack:
            vertex, color = stack.pop()

            if colors[vertex] != no_color:
                continue

            colors[vertex] = color

            if color == black:
                black_count += 1
            elif color == white:
                white_count += 1

            for to in graph[vertex]:
                if colors[to] == color:
                    return False, 0, 0

                if colors[to] == no_color:
                    stack.append((to, -color))  # Invert colors.

        return True, black_count, white_count

    for i in range(n):
        if colors[i] != no_color:
            continue

        flag, black_count, white_count = is_bipartite(
            start_id=i, graph=graph, colors=colors
        )

        # print(flag, black_count, white_count)

        if not flag:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
