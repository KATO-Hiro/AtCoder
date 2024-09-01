# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    s = [list(input().rstrip()) for _ in range(n)]
    pos = []

    for i in range(n):
        for j in range(n):
            if s[i][j] == "P":
                pos.append((i, j))

    # グリッドの状態を頂点とするグラフの最短経路問題に帰着 = BFS

    # 定数倍が重いので、座標のハッシュ値をキューに入れる
    # n進数に変換
    def to_hash(pos):
        p00, p01 = pos[0]
        p10, p11 = pos[1]

        value = p00
        value = value * n + p01
        value = value * n + p10
        value = value * n + p11

        return value

    def to_pos(hash):
        # to_hashとは逆順に
        p11 = hash % n
        hash //= n
        p10 = hash % n
        hash //= n

        p01 = hash % n
        hash //= n
        p00 = hash % n
        hash //= n

        pos = [(p00, p01), (p10, p11)]

        return pos

    n4 = n**4
    inf = 10**9

    dist = [inf] * n4
    id = to_hash(pos)
    dist[id] = 0

    q = deque([id])
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    while q:
        cur_id = q.popleft()
        pos = to_pos(cur_id)
        d = dist[cur_id]

        # グラフを陽に持たず、1手先の状態を用意
        for dx, dy in dxy:
            npos = []

            for y, x in pos:
                nx = x + dx
                ny = y + dy

                # 条件を満たしていなければ元に戻す
                if nx < 0 or nx >= n or ny < 0 or ny >= n or s[ny][nx] == "#":
                    nx, ny = x, y

                npos.append((ny, nx))

            nid = to_hash(npos)

            if dist[nid] != inf:
                continue

            dist[nid] = d + 1
            q.append(nid)

    ans = inf

    for id, di in enumerate(dist):
        pos = to_pos(id)

        if pos[0] == pos[1]:
            ans = min(ans, di)

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
