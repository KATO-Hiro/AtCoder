# -*- coding: utf-8 -*-


def main():
    a, b, c, d, e, f = map(int, input().split())
    ab = list()
    cd = list()

    for i in range(30 + 1):
        for j in range(30 + 1):
            if 100 * a * i + 100 * b * j <= f:
                ab.append((i, j))

    for x in range(100 + 1):
        for y in range(100 + 1):
            if c * x + d * y <= 30 * e:
                cd.append((x, y))

    ans = 0
    ans_water = 0
    ans_sugar = 0

    for i, j in ab:
        for x, y in cd:
            total_water = 100 * (a * i + b * j)
            total_sugar = c * x + d * y

            if total_water > 0 and total_water + total_sugar <= f and total_sugar <= e * total_water // 100:
                rate = 100 * total_sugar / (total_water + total_sugar)

                if rate - ans >= 0:
                    ans = rate
                    ans_water = total_water
                    ans_sugar = total_sugar

    print(ans_water + ans_sugar, ans_sugar)


if __name__ == '__main__':
    main()
