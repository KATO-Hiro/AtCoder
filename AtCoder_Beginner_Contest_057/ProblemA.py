'''input
23 2
1

9 12
21

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    current_hour, add_hour = list(map(int, input().split()))
    contest_hour = current_hour + add_hour

    if contest_hour < 24:
        print(contest_hour)
    else:
        print(contest_hour - 24)
