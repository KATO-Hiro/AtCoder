'''input
5
30 44
26
18
81
18
6

56

3
7 1
2
5
10

8

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    person_count = int(input())
    duration, x = map(int, input().split())
    a = [int(input()) for _ in range(person_count)]

    count = 0

    for i in a:
        y = 0

        while i * y + 1 <= duration:
            count += 1
            y += 1

    print(count + x)
