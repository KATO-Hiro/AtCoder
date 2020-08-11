'''input
3 3 4
2
22

5 3 11
1
30

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    numbers = sorted(list(map(int, input().split())))
    k = int(input())
    twice = numbers[2] * 2 ** k
    print(sum(numbers[:2]) + twice)
