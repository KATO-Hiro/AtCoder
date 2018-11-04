# -*- coding: utf-8 -*-


def main():
    a, b, c, d, e, f = map(int, input().split())
    concentration = 0
    water_set = set()
    sugar_set = set()

    # See:
    # https://www.youtube.com/watch?v=nCHz87GMdpo
    for i in range(f + 1):
        for j in range(f + 1):
            y = c * i + d * j

            if y <= f:
                sugar_set.add(y)

    for k in range(0, f + 1, 100):
        for l in range(0, f + 1, 100):
            x = a * k + b * l

            if 0 < x <= f:
                water_set.add(x)

    sugar_water_amount = min(water_set) + min(sugar_set)
    sugar_amount = min(sugar_set)

    for water in water_set:
        for sugar in sugar_set:
            if (water + sugar <= f) and (sugar <= e * (water // 100)):
                candidate = (100 * sugar) / (water + sugar)

                if candidate > concentration:
                    concentration = candidate
                    sugar_water_amount = water + sugar
                    sugar_amount = sugar

    print(sugar_water_amount, sugar_amount)


if __name__ == '__main__':
    main()
