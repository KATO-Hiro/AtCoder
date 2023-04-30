# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    c = [list(input().rstrip()) for _ in range(h)]
    n = min(h, w)
    ans = [0] * (n + 1)

    # グリッドの最も外側のマスは条件を必ず満たさないため、探索範囲から除外
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if c[y][x] == ".":
                continue

            if c[y + 1][x + 1] == c[y + 1][x - 1] == c[y - 1][x + 1] == c[y - 1][x - 1] == "#":
                count = 0

                # dを伸ばす
                for d in range(1, min(x, y) + 1):
                    if c[y - d][x - d] == ".":
                        break

                    count = d
                
                ans[count] += 1

    print(*ans[1:])
    

if __name__ == "__main__":
    main()
