'''input
8 6
Alice

1 1
Draw

13 1
Bob

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    card_orders = [number for number in range(2, 13 + 1)] + [1]
    a, b = list(map(int, input().split()))

    if card_orders.index(a) > card_orders.index(b):
        print('Alice')
    elif card_orders.index(a) < card_orders.index(b):
        print('Bob')
    else:
        print('Draw')
