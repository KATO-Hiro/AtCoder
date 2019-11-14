# -*- coding: utf-8 -*-


def main():
    x, y, w = input().split()
    cur_x, cur_y = int(x) - 1, int(y) - 1
    dx, dy = 0, 0
    c = [list(input()) for _ in range(9)]
    ans = c[cur_y][cur_x]

    # 方向指定からx方向とy方向に進むマスの数を計算
    if 'R' in w:
        dx = 1
    if 'L' in w:
        dx = -1

    if 'U' in w:
        dy = -1
    if 'D' in w:
        dy = 1

    while len(ans) < 4:
        nx = cur_x + dx
        ny = cur_y + dy

        # 端部に到達したときの処理
        # 反転して，移動させた分を元に戻す
        if nx < 0:
            dx *= -1
            nx += 2
        if 8 < nx:
            dx *= -1
            nx -= 2

        if ny < 0:
            dy *= -1
            ny += 2
        if 8 < ny:
            dy *= -1
            ny -= 2

        ans += c[ny][nx]

        cur_x = nx
        cur_y = ny

    print(ans)


if __name__ == '__main__':
    main()
