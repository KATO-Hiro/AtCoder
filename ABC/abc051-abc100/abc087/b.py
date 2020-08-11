# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    five_hundred_yen_count = int(input())
    one_hundred_yen_count = int(input())
    fifty_yen_count = int(input())
    total_yen = int(input())

    pattern_count = 0

    for i in range(five_hundred_yen_count + 1):
        for j in range(one_hundred_yen_count + 1):
            for k in range(fifty_yen_count + 1):
                summed_yen = 500 * i + 100 * j + 50 * k

                if total_yen - summed_yen == 0:
                    pattern_count += 1

    print(pattern_count)
