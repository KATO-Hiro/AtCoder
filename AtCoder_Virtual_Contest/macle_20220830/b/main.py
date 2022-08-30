# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    dxy = [(1, 0), (0, 1), (1, 1), (-1, 1)]

    # 6文字の判定部分を関数化
    def calc(x, y, dx, dy):
        count = 0

        # 範囲外の場合
        for i in range(6):
            if x < 0 or x >= n or y < 0 or y >= n:
                return False
        
            if s[y][x] == "#":
                count += 1

            x += dx
            y += dy
        
        return count >= 4

    for i in range(n):
        for j in range(n):
            for dx, dy in dxy:
                if calc(i, j, dx, dy):
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
