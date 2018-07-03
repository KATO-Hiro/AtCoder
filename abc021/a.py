'''input
1
1
1

5
3
1
2
2

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())
    count = 0
    number = [8, 4, 2, 1]
    pos = 0
    combinations = list()

    while n != 0 and n >= 0:
        while n >= number[pos]:
            n -= number[pos]
            combinations.append(number[pos])
            count += 1

        pos += 1

    print(count)

    for combination in combinations:
        print(combination)
