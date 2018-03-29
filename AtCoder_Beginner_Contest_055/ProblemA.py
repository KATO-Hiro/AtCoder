'''input
20
15800

60
47200

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    dish_count = int(input())

    paid_money_yen = dish_count * 800
    cash_back_yen = (dish_count // 15) * 200

    print(paid_money_yen - cash_back_yen)
