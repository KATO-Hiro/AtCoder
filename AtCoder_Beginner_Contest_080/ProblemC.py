'''input
1
1 1 0 1 0 0 0 1 0 1
3 4 5 6 7 8 9 -2 -3 4 -2
8

3
1 1 1 1 1 1 0 0 1 1
0 1 0 1 1 1 1 0 1 0
1 0 1 1 0 1 0 1 0 1
-8 6 -2 -8 -8 4 8 7 -6 2 2
-9 2 0 1 7 -5 0 -2 -6 5 5
6 -6 7 -9 6 -5 8 0 -9 -7 -7
23

2
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1
3 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
1

2
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
3 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
1

2
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
-2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


# FIXME: More smarter.
def calc_benefit(my_schedule, others_schedule, benefit_table, answer):
    score = 0

    if sum(my_schedule) == 0:
        return benefit_total

    for index, other_schedule in enumerate(others_schedule):
        count = 0

        for mine, other in zip(my_schedule, other_schedule):
            if mine == other == 1:
                count += 1
        score += benefit_table[index][count]
    return max(score, benefit_total)


# FIXME: More smarter.
def dfs(my_schedule, others_schedule, benefit_table, benefit_total, pos):
    if pos == 10:
        return calc_benefit(my_schedule, others_schedule, benefit_table, benefit_total)

    my_schedule[pos] = 0
    foo = dfs(my_schedule, others_schedule, benefit_table, benefit_total, pos + 1)
    my_schedule[pos] = 1
    bar = dfs(my_schedule, others_schedule, benefit_table, benefit_total, pos + 1)
    return max(foo, bar)


if __name__ == '__main__':
    shop_count = int(input())
    others_schedule = [list(map(int, input().split())) for _ in range(shop_count)]
    # working_days = [shop_working_table[i].count(1) for i in range(shop_count)]
    benefit_table = [list(map(int, input().split())) for _ in range(shop_count)]

    benefit_total = -1000000000
    my_schedule = [None] * (10)

    # See: https://www.youtube.com/watch?v=GWhYUxeDe70
    benefit_total = dfs(my_schedule, others_schedule, benefit_table, benefit_total, 0)
    print(benefit_total)

    # benefit_total = 0
    # including_closed = [max(benefit_table[j][:working_days[j] + 1]) for j in range(shop_count)]
    # open_only = [max(benefit_table[j][1:working_days[j] + 1]) for j in range(shop_count)]

    # for k in range(shop_count):
    #     if k == open_only.index(max(open_only)):
    #         benefit_total += max(open_only)
    #     else:
    #         benefit_total += max(including_closed[k], open_only[k])

    # FIXME: some tests have failed.
    # print(benefit_total)
