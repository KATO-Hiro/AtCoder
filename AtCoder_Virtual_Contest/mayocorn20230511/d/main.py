# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    large_h, large_w, n, h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(large_h)]
    # グリッド全体の数字の種類と個数 - 塗りつぶし部分の数字の種類と個数
    all_count = defaultdict(int)

    for i in range(large_h):
        for j in range(large_w):
            all_count[a[i][j]] += 1

    ans = list()

    # 差分を計算
    for k in range(large_h - h + 1):
        part_count = defaultdict(int)
        tmp = list()

        for l in range(large_w - w + 1):
            if l == 0:
                for i in range(k, k + h):
                    for j in range(l, l + w):
                        part_count[a[i][j]] += 1
            else:
                for i in range(k, k + h):
                    part_count[a[i][l - 1]] -= 1
                    part_count[a[i][l + w - 1]] += 1

            count = 0

            for key, value in all_count.items():
                if key not in part_count.keys():
                    count += 1
                else:
                    if all_count[key] - part_count[key] >= 1:
                        count += 1

            tmp.append(count)

        ans.append(tmp)

    for ai in ans:
        print(*ai)


if __name__ == "__main__":
    main()
