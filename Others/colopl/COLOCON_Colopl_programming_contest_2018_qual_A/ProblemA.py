'''input
2 7
kitayuta
NO

4 8
colopl
YES

'''

# -*- coding: utf-8 -*-

# COLOCON Colopl programming contest 2018 qual A
# Problem A

if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    s = input()

    if a <= len(s) <= b:
        print('YES')
    else:
        print('NO')
