# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])

    for x in range(h):
        for y in range(w):
            pos = a[x][y]

            if pos >= 0:
                ans += c[pos][1]

    print(ans)


if __name__ == '__main__':
    main()
