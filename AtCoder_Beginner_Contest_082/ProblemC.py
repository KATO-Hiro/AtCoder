'''input
4
3 3 3 3
1

5
2 4 1 4 2
2

6
1 2 2 3 3 3
0

1
1000000000
1

8
2 7 1 8 2 8 1 8
5

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    from collections import Counter
    counted_a = Counter(a)

    for x in counted_a:
            if counted_a[x] >= x:
                count += counted_a[x] - x
            else:
                count += counted_a[x]

    print(count)
