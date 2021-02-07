# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0

    for i in range(h - 1):
        for j in range(w - 1):
            count = 0

            for ni, nj in [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                if s[ni][nj] == "#":
                    count += 1

            if count % 2 == 1:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
