'''input
5
1 2 3 4 5
NO

1
1
YES

3
1 2 3
YES

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    odd_count = 0

    for ai in a:
        if ai % 2 == 1:
            odd_count += 1

    even_count = n - odd_count

    if odd_count % 2 == 1:
        if even_count > 0:
            print('NO')
            exit()
        elif even_count == 0 and odd_count == 1:
            print('NO')
            exit()
        else:
            print('YES')
            exit()
    else:
        print('YES')
        exit()
