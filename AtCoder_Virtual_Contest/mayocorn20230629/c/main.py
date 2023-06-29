# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(input().rstrip()) for _ in range(n)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    ans = set()

    for i in range(n):
        for j in range(n):
            for dx, dy in dxy:
                candidate = list()

                for k in range(n):
                    nx = (j + dx * k) % n
                    ny = (i + dy * k) % n
                    candidate.append(a[ny][nx])

                ans.add(int("".join(candidate)))

    print(max(ans))


if __name__ == "__main__":
    main()
