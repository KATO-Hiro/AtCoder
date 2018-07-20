'''input
3
2 1 4
2
1 1
2 3

6
9

5
7 2 3 8 5
3
4 2
1 7
4 13

19
25
30
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    problem_count = int(input())
    elapsed_times = list(map(int, input().split()))
    drink_kind_count = int(input())
    effects = [list(map(int, input().split())) for i in range(drink_kind_count)]

    total_elapsed_time = sum(elapsed_times)

    for problem_p, new_elapsed_time, in effects:
        print(total_elapsed_time + (new_elapsed_time - elapsed_times[problem_p - 1]))
