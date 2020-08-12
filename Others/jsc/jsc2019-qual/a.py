# -*- coding: utf-8 -*-


def main():
    m, d = map(int, input().split())
    ans = 0

    for mi in range(1, m + 1):
        for di in range(1, d + 1):
            d10 = di // 10
            d1 = di - d10 * 10

            if mi == d1 * d10 and d1 >= 2 and d10 >= 2:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
