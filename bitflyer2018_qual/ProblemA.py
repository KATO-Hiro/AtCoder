'''input
56
1
56

79
6
78

100
100
100

'''

# -*- coding: utf-8 -*-

# bitflyer2018 qual
# Problem A

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    for i in range(a, -1, -1):
        if i % b == 0:
            print(i)
            exit()
