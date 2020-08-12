'''input
111100
4

'''

# -*- coding: utf-8 -*-

# tenka1 2016 qual A
# Problem A

if __name__ == '__main__':
    total = 0

    for i in range(1, 100 + 1):
        if i % 3 != 0 and i % 5 != 0:
            total += i

    print(total)
