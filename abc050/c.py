'''input
5
2 4 4 0 2
4

7
6 4 0 2 4 0 2
0

8
7 5 1 1 7 3 5 3
16

4
3 3 3 1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from collections import Counter

    person_count = int(input())
    relative_positions = Counter(map(int, input().split()))

    if person_count % 2 == 0:
        for key, value in relative_positions.items():
            if (key % 2 == 0) or (value != 2):
                print(0)
                exit()
    else:
        for key, value in relative_positions.items():
            if (key % 2 == 1) or (key == 0 and value != 1) or (key != 0 and value != 2):
                print(0)
                exit()

    print(2 ** (person_count // 2) % (10 ** 9 + 7))
