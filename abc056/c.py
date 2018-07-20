'''input
1000000000

6
3

2
2

11
5

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    x = int(input())

    i = 1
    pre = 0
    current = i

    while True:
        if pre < x <= current:
            print(i)
            exit()

        pre = current
        i += 1
        current += i
