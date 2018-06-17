'''input
97
89
20000
25899

10
5
8
10

97
89
8634
17266

97
89
8633
8633

100
100
101
200

1
1
1
1

1
1
20000
20000

100
100
20000
20000

12
8
25
48

2
3
8
12

2
2
2
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    n = int(input())

    # See:
    # https://beta.atcoder.jp/contests/abc032/submissions/2264731
    for i in range(n, 30000 + 1):
        if i % a == 0 and i % b == 0:
            print(i)
            exit()
