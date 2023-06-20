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

    ans = 0

    for i in range(n):
        count = 0

        for j in graph[i]:
            if j < i:
                count += 1

        if count == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
