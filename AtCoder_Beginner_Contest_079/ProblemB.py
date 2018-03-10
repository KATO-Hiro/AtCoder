'''input
1
86
939587134549734843
5
11
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    number = int(input())
    lucas_numbers = [2, 1]

    if number >= 2:
        for i in range(2, number + 1):
            new_value = lucas_numbers[i - 1] + lucas_numbers[i - 2]
            lucas_numbers.append(new_value)

        print(lucas_numbers[number])
    else:
        print(lucas_numbers[1])
