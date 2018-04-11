'''input
3242
3+2+4-2=7

1222
1+2+2+2=7

0290
0-2+9+0=7

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    numbers = list(map(int, list(input())))
    result = '=7'
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    d = numbers[3]
    total = 7

    # FIME: More smartly.
    if a + b + c + d == total:
        print(str(a) + '+' + str(b) + '+' + str(c) + '+' + str(d) + result)
    elif a + b + c - d == total:
        print(str(a) + '+' + str(b) + '+' + str(c) + '-' + str(d) + result)
    elif a + b - c + d == total:
        print(str(a) + '+' + str(b) + '-' + str(c) + '+' + str(d) + result)
    elif a + b - c - d == total:
        print(str(a) + '+' + str(b) + '-' + str(c) + '-' + str(d) + result)
    elif a - b + c + d == total:
        print(str(a) + '-' + str(b) + '+' + str(c) + '+' + str(d) + result)
    elif a - b + c - d == total:
        print(str(a) + '-' + str(b) + '+' + str(c) + '-' + str(d) + result)
    elif a - b - c + d == total:
        print(str(a) + '-' + str(b) + '-' + str(c) + '+' + str(d) + result)
    elif a - b - c - d == total:
        print(str(a) + '-' + str(b) + '-' + str(c) + '-' + str(d) + result)
