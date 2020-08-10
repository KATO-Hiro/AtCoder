# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    dxy = [(0, 1), (0, -1), (1, -1), (1, 0),
           (1, 1), (-1, -1), (-1, 0), (-1, 1)]
    ans = [['.' for _ in range(w)] for _ in range(h)]
    validate = [['.' for _ in range(w)] for _ in range(h)]

    for cur_y in range(h):
        for cur_x in range(w):
            seen_count = 0
            black_count = 0

            if s[cur_y][cur_x] == '.':
                continue

            seen_count += 1
            black_count += 1

            # 8方向調べる
            for dx, dy in dxy:
                nx = cur_x + dx
                ny = cur_y + dy

                # 範囲外参照を回避
                if nx < 0 or w <= nx or ny < 0 or h <= ny:
                    continue

                seen_count += 1

                if s[ny][nx] == '#':
                    black_count += 1

            if seen_count == black_count:
                ans[cur_y][cur_x] = '#'

    # 収縮前後の結果を比較
    for cur_y in range(h):
        for cur_x in range(w):
            if ans[cur_y][cur_x] == '#':
                validate[cur_y][cur_x] = '#'

            # 8方向調べる
            for dx, dy in dxy:
                nx = cur_x + dx
                ny = cur_y + dy

                # 範囲外参照を回避
                if nx < 0 or w <= nx or ny < 0 or h <= ny:
                    continue

                if ans[ny][nx] == '#':
                    validate[cur_y][cur_x] = '#'

    if validate == s:
        print('possible')

        for a in ans:
            print(''.join(map(str, a)))

    else:
        print('impossible')


if __name__ == '__main__':
    main()
