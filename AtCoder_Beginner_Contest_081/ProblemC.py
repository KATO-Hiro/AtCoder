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
    sorted_ball_numbers = sorted(ball_numbers.items(), key=lambda x: x[1])
    ball_number_key_count = len(ball_numbers.keys())

    need_rewritten_count = 0
    diff_count = ball_number_key_count - kind_count

    if diff_count > 0:
        for i, (key, value) in enumerate(sorted_ball_numbers):
            if diff_count > i:
                need_rewritten_count += value

    print(need_rewritten_count)
