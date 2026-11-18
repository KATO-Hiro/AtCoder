# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    ans = []

    for j in range(w):
        count = 0

        for i in range(h):
            if s[i][j] != "#":
                continue

            count += 1

        ans.append(count)

    print(*ans)


if __name__ == "__main__":
    main()
