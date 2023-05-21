# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

    from typing import List

    def is_in_grid(nx: int, ny: int, w: int = w, h: int = h) -> bool:
        if not (0 <= nx < w):
            return False
        if not (0 <= ny < h):
            return False

        return True

    def is_exist_word_in_grid(grid: List[str], word: str):
        word_size = len(list(word))

        for dx, dy in dxy:
            for y in range(h):
                for x in range(w):
                    candidate = ""
                    pos = list()  # y, x

                    for k in range(word_size):
                        nx, ny = x + dx * k, y + dy * k

                        if not is_in_grid(nx, ny):
                            continue

                        candidate += grid[ny][nx]
                        pos.append((ny + 1, nx + 1))

                    if candidate == word:
                        return True, pos

        return False, []

    _, pos = is_exist_word_in_grid(s, "snuke")

    for ri, ci in pos:
        print(ri, ci)


if __name__ == "__main__":
    main()
