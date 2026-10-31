# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    size = 5
    s = [list(input().rstrip()) for _ in range(size)]
    ans = size

    for i in range(size):
        count = 0

        for j in range(size):
            if s[i][j] == "o":
                continue

            count += 1

        ans = min(ans, count)

    for j in range(size):
        count = 0

        for i in range(size):
            if s[i][j] == "o":
                continue

            count += 1

        ans = min(ans, count)

    count = 0

    for i in range(size):
        if s[i][i] == "o":
            continue

        count += 1

    ans = min(ans, count)

    count = 0

    for i in range(size):
        if s[i][size - i - 1] == "o":
            continue

        count += 1

    ans = min(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
