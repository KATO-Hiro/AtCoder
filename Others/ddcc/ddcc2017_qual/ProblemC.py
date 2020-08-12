'''input
10 30
22
5
2
18
6
21
28
11
18
1
5

9 30
22
5
2
18
6
21
29
11
18
5

4 10
2
8
4
5
3

3 10
1
1
1
2

'''

# -*- coding: utf-8 -*-

# ddcc2017 qual
# Problem C

if __name__ == '__main__':
    n, c = list(map(int, input().split()))
    l = sorted([int(input()) for _ in range(n)], reverse=True)
    count = 0
    i = 0
    j = n - 1

    while i <= j and l[j] != 0:
        if l[i] + l[j] + 1 <= c:
            l[j] = 0
            j -= 1

        i += 1
        count += 1

    print(count)
