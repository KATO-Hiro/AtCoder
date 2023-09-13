# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    grid = [
        list("###############"),
        list("#.............#"),
        list("#.###########.#"),
        list("#.#.........#.#"),
        list("#.#.#######.#.#"),
        list("#.#.#.....#.#.#"),
        list("#.#.#.###.#.#.#"),
        list("#.#.#.#.#.#.#.#"),
        list("#.#.#.###.#.#.#"),
        list("#.#.#.....#.#.#"),
        list("#.#.#######.#.#"),
        list("#.#.........#.#"),
        list("#.###########.#"),
        list("#.............#"),
        list("###############"),
    ]

    r, c = map(int, input().split())
    r -= 1
    c -= 1

    color = grid[r][c]

    if color == "#":
        print("black")
    else:
        print("white")


if __name__ == "__main__":
    main()
