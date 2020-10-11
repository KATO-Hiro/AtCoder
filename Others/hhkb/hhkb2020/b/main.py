# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    count = 0

    for i in range(h):
        for first, second in zip(s[i], s[i][1:]):
            if first == second == ".":
                count += 1

    for i in range(h - 1):
        for j in range(w):
            if s[i][j] == s[i + 1][j] == ".":
                count += 1

    print(count)


if __name__ == "__main__":
    main()
