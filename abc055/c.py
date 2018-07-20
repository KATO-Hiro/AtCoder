'''input
1000000000000 1000000000000
500000000000

123124134 89879876
44939938

1 1000000000000
250000000000

2 1000000000000
250000000001

2 1
1

1 2
1

1 6
2

678901 12345
175897

12345 678901
175897

1 1
0

1000000000000 1
0

8 5
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    # See:
    # https://www.youtube.com/watch?v=hetSRNLGOtk
    print(min(m // 2, (2 * n + m) // 4))
