# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for j in range(w - 1):
        for i in range(h - 1):
            diff = a[i][j] - b[i][j]

            if diff == 0:
                continue

            ans += abs(diff)

            for dx in range(2):
                for dy in range(2):
                    ni, nj = i + dy, j + dx
                    a[ni][nj] -= diff

    for i in range(h):
        for j in range(w):
            if a[i][j] != b[i][j]:
                print("No")
                exit()

    print("Yes")
    print(ans)


if __name__ == "__main__":
    main()
