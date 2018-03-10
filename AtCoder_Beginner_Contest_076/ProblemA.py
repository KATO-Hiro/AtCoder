'''input
4500
0
-4500
2002
2017
2032
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    current_rating = int(input())
    target_rating = int(input())

    result = 2 * target_rating - current_rating
    print(result)
