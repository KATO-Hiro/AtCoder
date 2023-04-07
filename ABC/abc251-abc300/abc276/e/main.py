# -*- coding: utf-8 -*-


class UnionFind:
    def __init__(self, number_count: int):
        self.parent_numbers = [-1 for _ in range(number_count)]

    def find_root(self, number: int) -> int:
        if self.parent_numbers[number] < 0:
            return number

        self.parent_numbers[number] = self.find_root(self.parent_numbers[number])
        return self.parent_numbers[number]

    def merge_if_needs(self, number_x: int, number_y: int) -> bool:
        x = self.find_root(number_x)
        y = self.find_root(number_y)

        if x == y:
            return False

        if self.parent_numbers[x] > self.parent_numbers[y]:
            x, y = y, x

        self.parent_numbers[x] += self.parent_numbers[y]
        self.parent_numbers[y] = x
        return True


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    n = h * w + 1
    uf = UnionFind(n)

    def to_id(i, j):
        return i * w + j

    # Sに隣接する4マスのうち異なる2マスを行き来できるか?
    # 連結性の判定問題と言い換え
    sx, sy = -1, -1

    for i in range(h):
        for j in range(w):
            if s[i][j] == "S":
                sx, sy = j, i

            if s[i][j] != ".":
                continue

            # 着目しているマスの右と下のみチェックすれば十分
            if (i + 1 < h) and s[i + 1][j] == ".":
                uf.merge_if_needs(to_id(i, j), to_id(i + 1, j))
            if (j + 1 < w) and s[i][j + 1] == ".":
                uf.merge_if_needs(to_id(i, j), to_id(i, j + 1))

    # leaderが一つでも一致しているか?
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count, leaders = 0, set()

    for dx, dy in dxy:
        nx, ny = sx + dx, sy + dy
    
        if ny < 0 or ny >= h:
            continue
        if nx < 0 or nx >= w:
            continue
        if s[ny][nx] == "#":
            continue

        leaders.add(uf.find_root(to_id(ny, nx)))
        count += 1
    
    if len(leaders) == count:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
