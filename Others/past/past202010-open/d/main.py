# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(input())
    count = n
    x, y = 0, 0

    for i in range(100):
        for index in range(n - 1, 0, -1):
            if s[index] == ".":
                continue

            ni = index - 1

            if 0 <= ni and s[ni] == ".":
                s[ni] = "#"
                x += 1
                count -= 1

        for index, si in enumerate(s):
            if si == ".":
                continue

            ni = index + 1

            if ni < n and s[ni] == ".":
                s[ni] = "#"
                y += 1
                count -= 1

    print(x, y)


if __name__ == "__main__":
    main()
