'''input
4 4
1 1 2 2
0

10 3
5 1 3 2 4 1 1 2 3 4
3

5 2
1 1 2 2 5
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from collections import Counter

    ball_count, kind_count = map(int, input().split())
    ball_numbers = Counter(list(map(int, input().split())))
    ball_number_key_count = len(ball_numbers.keys())

    sorted_ball_numbers = sorted(ball_numbers.values())
    print(sum(sorted_ball_numbers[:-kind_count]))
