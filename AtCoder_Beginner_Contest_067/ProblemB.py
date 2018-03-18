'''input
15 14
50 26 27 21 41 7 42 35 7 5 5 36 39 1 45

386

5 3
1 2 3 4 5

12

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    total_bar_count, choosed_bar_count = list(map(int, input().split()))
    bar_lengths = list(map(int, input().split()))

    bar_lengths.sort(reverse=True)
    total_bar_length = sum(bar_lengths[:choosed_bar_count])
    print(total_bar_length)
