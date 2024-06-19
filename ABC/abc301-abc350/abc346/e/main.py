# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, m = map(int, input().split())
    tax = list()

    for i in range(m):
        tax.append(list(map(int, input().split())))

    colors = defaultdict(int)
    remain_h, remain_w = h, w
    used_h, used_w = [False] * h, [False] * w

    # 後の操作が優先される場合は、逆順にみる
    # 行単位 / 列単位で更新する場合は、行列を入れ替えても結果が変わらないことを利用
    for i in range(m - 1, -1, -1):
        ti, ai, xi = tax[i]
        ai -= 1

        if ti == 1:
            if used_h[ai]:
                continue

            used_h[ai] = True

            colors[xi] += remain_w
            remain_h -= 1
        else:
            if used_w[ai]:
                continue

            used_w[ai] = True

            colors[xi] += remain_h
            remain_w -= 1

    # 左上の領域の0の個数を追加
    colors[0] += remain_h * remain_w
    ans = list()

    for key in sorted(colors.keys()):
        count = colors[key]

        if count > 0:
            ans.append((key, count))

    print(len(ans))

    for key, count in ans:
        print(key, count)


if __name__ == "__main__":
    main()
