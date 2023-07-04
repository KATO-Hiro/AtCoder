# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    a, n = map(int, input().split())

    # 整数に対する操作を有向グラフと捉えて、最短経路問題に帰着
    q = deque([1])
    size = 10**6
    cost = [-1] * size
    cost[1] = 0  # Initialize

    while q:
        x = q.popleft()
        nx = x * a

        if nx < size and cost[nx] == -1:
            cost[nx] = cost[x] + 1
            q.append(nx)

        if len(str(x)) >= 2 and x % 10 != 0:
            tmp = str(x)
            nx = int(tmp[-1] + tmp[:-1])

            if nx < size and cost[nx] == -1:
                cost[nx] = cost[x] + 1
                q.append(nx)

    print(cost[n])


if __name__ == "__main__":
    main()
