# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    total_money = int(input())
    one_yen_count = int(input())

    balance = total_money % 500

    if one_yen_count - balance >= 0:
        print('Yes')
    else:
        print('No')
