'''input
8 8
1 2
3 4
1 5
2 8
3 7
5 2
4 1
6 8

3
3
2
2
2
1
1
2

4 3
1 2
2 3
1 4

2
2
1
1

2 5
1 2
2 1
1 2
2 1
1 2

5
5

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    city_count, road_count = map(int, input().split())
    a = list()
    b = list()

    for _ in range(road_count):
        line = input().split()
        a.append(line[0])
        b.append(line[1])

    for i in range(1, city_count + 1):
        link_count = a.count(str(i)) + b.count(str(i))
        print(link_count)
