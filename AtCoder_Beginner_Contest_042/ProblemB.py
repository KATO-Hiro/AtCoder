'''input
3 3
dxx
axx
abx
abxaxxdxx

3 3
dxx
axx
cxx
axxcxxdxx

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    n, length = list(map(int, input().split()))
    s = sorted([input() for _ in range(n)])

    print(''.join(s))
