'''input
9 45000
4 0 5

20 196000
-1 -1 -1

1000 1234000
14 27 959

2000 20000000
2000 0 0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    bill_count, total_yen = list(map(int, input().split()))
    bill_max = 2000

    five_thousand_yen_count = 0
    one_thousand_yen_count = 0

    for z in range(bill_max + 1):
        for y in range(bill_max + 1):
            if (5 * y + 9 * z) == (10 * bill_count - total_yen / (10 ** 3)):
                five_thousand_yen_count = y
                one_thousand_yen_count = z
                break

    ten_thousand_yen_count = bill_count - (five_thousand_yen_count + one_thousand_yen_count)

    condition = ((10 * ten_thousand_yen_count) + (5 * five_thousand_yen_count) + one_thousand_yen_count) == (total_yen / 1000)
    condition1 = ten_thousand_yen_count >= 0
    condition2 = five_thousand_yen_count >= 0
    condition3 = one_thousand_yen_count >= 0

    if condition and condition1 and condition2 and condition3:
        print(str(ten_thousand_yen_count) + ' ' + str(five_thousand_yen_count) + ' ' + str(one_thousand_yen_count))
    else:
        print('-1 -1 -1')
