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
    numbers = list(input())
    result = '=7'
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    d = numbers[3]

    # See:
    # https://abc079.contest.atcoder.jp/submissions/1917934
    ops = ['+', '-']

    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                expression = a + op1 + b + op2 + c + op3 + d
                if eval(expression) == 7:
                    print(expression + '=7')
                    exit()
