# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    # Input
    pocket_money_yen = int(input())
    cake_price_yen = int(input())
    doughnut_price_yen = int(input())

    balance = pocket_money_yen - cake_price_yen
    balance = balance % doughnut_price_yen

    # Output
    print(balance)
