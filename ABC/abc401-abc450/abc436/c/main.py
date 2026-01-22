# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = set()
    dxy = [(0, 0), (1, 0), (0, 1), (1, 1)]
    ans = 0

    for _ in range(m):
        ri, ci = map(int, input().split())
        ok = True

        for dx, dy in dxy:
            ny, nx = ri + dy, ci + dx

            if (ny, nx) in s:
                ok = False
                break

        if ok:
            ans += 1

            for dx, dy in dxy:
                ny, nx = ri + dy, ci + dx
                s.add((ny, nx))

    print(ans)


if __name__ == "__main__":
    main()
