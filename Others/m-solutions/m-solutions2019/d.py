# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n = int(input())
    graph = [list() for _ in range(n)]

    for i in range(n - 1):
        ai, bi = map(int, input().split())
        graph[ai - 1].append(bi - 1)
        graph[bi - 1].append(ai - 1)

    c = sorted(list(map(int, input().split())), reverse=True)

    # スコアの最大値：数列cのうち，最大値を除いた合計
    print(sum(c[1:]))

    # 書き込み方：根から大きな値を割り当てるとよさそう
    visited = [False for _ in range(n)]
    visited[0] = True
    d = deque()
    d.append(0)
    ans = [0 for _ in range(n)]
    ans[0] = c[0]
    count = 1

    while d:
        di = d.popleft()

        for dii in graph[di]:
            if not visited[dii]:
                ans[dii] = c[count]
                count += 1
                visited[dii] = True
                d.append(dii)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
