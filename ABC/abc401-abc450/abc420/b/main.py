# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    count = [0] * n

    for j in range(m):
        x, y = 0, 0

        for i in range(n):
            if s[i][j] == "0":
                x += 1
            else:
                y += 1

        if x == 0 or y == 0:
            for i in range(n):
                count[i] += 1
        elif x < y:
            for i in range(n):
                if s[i][j] == "0":
                    count[i] += 1
        elif x > y:
            for i in range(n):
                if s[i][j] == "1":
                    count[i] += 1

    count_max = max(count)
    ans = []

    for i in range(n):
        if count[i] == count_max:
            ans.append(i + 1)

    print(*ans)


if __name__ == "__main__":
    main()
