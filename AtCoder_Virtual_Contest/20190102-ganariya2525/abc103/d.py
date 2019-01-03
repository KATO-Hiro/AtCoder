# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    ab = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[1])
    ans = 1
    axis = ab[0][1]

    for i in range(1, m):
        if ab[i][0] >= axis:
            ans += 1
            axis = ab[i][1]

    print(ans)


if __name__ == '__main__':
    main()
