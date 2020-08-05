# -*- coding: utf-8 -*-


def warshall_floyd(dist):
    v_count = len(dist[0])

    for k in range(v_count):
        for i in range(v_count):
            for j in range(v_count):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    results = warshall_floyd(c)

    for i in range(h):
        for j in range(w):
            if a[i][j] != -1:
                ai = a[i][j]
                ans += results[ai][1]

    print(ans)


if __name__ == '__main__':
    main()
