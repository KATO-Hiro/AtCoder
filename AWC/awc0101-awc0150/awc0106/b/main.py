# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    hw = []

    for i, hi in enumerate(h):
        hw.append((hi, i))

    hw.sort(key=lambda x: -x[0])

    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        if h[ai] > h[bi]:
            graph[ai].append(bi)
        elif h[ai] < h[bi]:
            graph[bi].append(ai)

    s = set(map(lambda x: int(x) - 1, input().split()))

    for hi, cur in hw:
        if cur in s:
            continue

        count = len(graph[cur])

        if count == 0:
            continue

        wj = w[cur] / count

        for to in graph[cur]:
            w[to] += wj

        w[cur] = 0.0

    print(*w)


if __name__ == "__main__":
    main()
