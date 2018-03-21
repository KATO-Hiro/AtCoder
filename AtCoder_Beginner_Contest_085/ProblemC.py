'''input
9 45000
4 0 5

20 196000
-1 -1 -1

1000 1234000
14 27 959

2000 20000000
2000 0 0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    bill_count, total_yen = list(map(int, input().split()))

    # See:https://beta.atcoder.jp/contests/abc085/submissions/1967109

    for i in range(bill_count + 1):
        for j in range(bill_count - i + 1):
            if (10 * i + 5 * j + (bill_count - i - j)) == total_yen // 1000:
                print(i, j, bill_count - i - j)
                exit()
    else:
        print('-1 -1 -1')
