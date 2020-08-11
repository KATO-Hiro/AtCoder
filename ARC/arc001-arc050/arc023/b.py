# -*- coding: utf-8 -*-


def main():
    r, c, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(r)]
    ans = 0

    # See:
    # https://www.slideshare.net/chokudai/arc023
    for y in range(r):
        for x in range(c):
            if (x + y <= d) and ((x + y) % 2 == d % 2):
                ans = max(ans, a[y][x])

    print(ans)


if __name__ == '__main__':
    main()
