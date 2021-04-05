# -*- coding: utf-8 -*-


def main():
    h, w, x, y = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    x -= 1
    y -= 1
    count = 0

    for i in range(x, h):
        if s[i][y] == ".":
            count += 1
        else:
            break

    for i in range(x, -1, -1):
        if s[i][y] == ".":
            count += 1
        else:
            break

    for j in range(y, w):
        if s[x][j] == ".":
            count += 1
        else:
            break

    for j in range(y, -1, -1):
        if s[x][j] == ".":
            count += 1
        else:
            break

    print(max(0, count - 3))


if __name__ == "__main__":
    main()
