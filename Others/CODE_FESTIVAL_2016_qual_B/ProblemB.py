'''input
5 2 2
ccccc
No
No
No
No
No

10 2 3
abccabaabb
Yes
Yes
No
No
Yes
Yes
Yes
No
No
No

12 5 2
cabbabaacaba
No
Yes
Yes
Yes
Yes
No
Yes
Yes
No
Yes
No
No

'''

# -*- coding: utf-8 -*-

# CODE FESTIVAL 2016 qual B
# Problem B

if __name__ == '__main__':
    n, a, b = list(map(int, input().split()))
    s = input()
    a_count = 0
    b_count = 0
    a_b_count = 0

    for si in s:
        if (si == 'a') and (a_b_count < a + b):
            a_count += 1
            print('Yes')
        elif (si == 'b') and (a_b_count < a + b) and (b_count < b):
            b_count += 1
            print('Yes')
        else:
            print('No')

        a_b_count = a_count + b_count
