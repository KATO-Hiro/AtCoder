# -*- coding: utf-8 -*-


def is_on_circle(xi, yi, ri, x, y):
    if (x - xi) ** 2 + (y - yi) ** 2 == ri ** 2:
        return True
    else:
        return False


def is_hit(xi, yi, ri, xj, yj, rj):
    dist = abs(xi - xj) ** 2 + abs(yi - yj) ** 2

    if (max(ri, rj) - min(ri, rj)) ** 2 <= dist <= (ri + rj) ** 2:
        return True
    else:
        return False


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [tuple(map(int, input().split())) for _ in range(n)]
    graph = [[] for _ in range(n)]
    cs, ct = -1, -1 # s, tがどの円に属するか

    # 始点・終点がどの円に属するか判定
    for i in range(n):
        xi, yi, ri = xyr[i]

        if is_on_circle(xi, yi, ri, sx, sy):
            cs = i
        if is_on_circle(xi, yi, ri, tx, ty):
            ct = i
    
    # 始点・終点が同じ円に属する
    if cs == ct:
        print("Yes")
        exit()
    
    # 円同士が接するか判定
    for i in range(n):
        xi, yi, ri = xyr[i]

        for j in range(i + 1, n):
            xj, yj, rj = xyr[j]

            if is_hit(xi, yi, ri, xj, yj, rj):
                graph[i].append(j)
                graph[j].append(i)
    
    # sからtへ移動できるかBFSで判定
    d = deque()
    d.append(cs)
    used = [False] * n

    while d:
        di = d.popleft()

        if di == ct:
            print("Yes")
            exit()

        if used[di]:
            continue

        used[di] = True

        for to in graph[di]:
            if used[to]:
                continue

            d.append(to)

    print("No")


if __name__ == "__main__":
    main()
