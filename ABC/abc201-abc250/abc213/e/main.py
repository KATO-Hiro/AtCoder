# -*- coding: utf-8 -*-


def main():
    from collections import deque

    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    inf = 10 ** 10
    costs = [[inf for _ in range(w)] for _ in range(h)]
    costs[0][0] = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = deque()
    d.append((0, 0))

    while d:
        cur_y, cur_x = d.popleft()
        
        if visited[cur_y][cur_x]:
            continue

        visited[cur_y][cur_x] = True
        cost = costs[cur_y][cur_x]

        # 壁を破壊せずに移動
        for dx, dy in dxy:
            nx = cur_x + dx
            ny = cur_y + dy

            if nx < 0 or nx >= w:
                continue
            if ny < 0 or ny >= h:
                continue
            if s[ny][nx] == '#':
                continue                   
            if costs[ny][nx] <= cost:
                continue

            costs[ny][nx] = cost
            d.appendleft((ny, nx))
        
        # 壁を破壊して移動
        for dx2 in range(-2, 3):
            for dy2 in range(-2, 3):
                # マンハッタン距離が3より大きい
                if abs(dy2) + abs(dx2) > 3:
                    continue
                
                nx2 = cur_x + dx2
                ny2 = cur_y + dy2

                if nx2 < 0 or nx2 >= w:
                    continue
                if ny2 < 0 or ny2 >= h:
                    continue
                if costs[ny2][nx2] <= cost + 1:
                    continue

                costs[ny2][nx2] = cost + 1
                d.append((ny2, nx2))


    print(costs[h - 1][w - 1])


if __name__ == "__main__":
    main()
