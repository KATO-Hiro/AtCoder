'''input
1000 1234000
14 27 959

2000 20000000
2000 0 0

9 45000
4 0 5

20 196000
-1 -1 -1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    osatsu_count, total_money = list(map(int, input().split()))

    shotage_osatsu_count = int(total_money / 1000) - osatsu_count

    mod_x = 0
    mod_y = 0

    for x in range(osatsu_count + 1):
        for y in range(osatsu_count + 1):
            if (9 * x + 4 * y) == shotage_osatsu_count:
                mod_x = x
                mod_y = y
                break

    z = osatsu_count - (mod_x + mod_y)

    if ((mod_x + mod_y + z) == osatsu_count) \
        and ((mod_x >= 0) and (mod_y >= 0) and (z >= 0)) \
        and ((10 * mod_x + 5 * mod_y + z) == int(total_money / 1000)):
        print(str(mod_x) + ' ' + str(mod_y) + ' ' + str(z))
    else:
        print('-1 -1 -1')
