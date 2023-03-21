# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    h, w, n, dh, dw = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    d = defaultdict(int)

    # 全体: 数字の個数を数える
    for i in range(h):
        for j in range(w):
            d[a[i][j]] += 1
    
    # 塗りつぶした部分の数字の個数を数える
    for k in range(h - dh + 1):
        d_filled = defaultdict(int)
        count = 0
        ans = list()

        # dh * dw
        for y in range(k, dh + k):
            for x in range(dw):
                d_filled[a[y][x]] += 1
        
        for key, value in d.items():
            if value > d_filled[key]:
                count += 1
        
        ans.append(count)
    
        # 差分のみ更新
        for l in range(w - dw):
            count = 0

            for hi in range(k, dh + k):
                d_filled[a[hi][l]] -= 1
                d_filled[a[hi][l + dw]] += 1

            for key, value in d.items():
                if value > d_filled[key]:
                    count += 1

            ans.append(count)
    
        print(*ans)


if __name__ == "__main__":
    main()
