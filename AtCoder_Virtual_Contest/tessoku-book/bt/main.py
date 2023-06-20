# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    c = [list(input().rstrip()) for _ in range(h)]
    ans = 0

    # bit全探索で行全体を黒に変更する回数x + k - x列全体を黒に変更
    # 列の候補: 行全体を黒マスに変更したときの増分の大きいもの
    for pattern in product([0, 1], repeat=h):
        remain = k - sum(pattern)

        if remain < 0:
            continue

        cell_count = list()

        for j in range(w):
            black = 0

            for i, pi in enumerate(pattern):
                if c[i][j] == "#":
                    black += 1
                elif pi == 1:
                    black += 1

            cell_count.append((black, j))

        cell_count = sorted(cell_count)
        count = 0

        for i, (black, j) in enumerate(cell_count):
            if i < remain:
                count += h
            else:
                count += black

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
