'''input
yyyyy
NO

yahoo
YES

snuke
NO

'''

# -*- coding: utf-8 -*-

# yahoo procon2018 qual
# Problem A

if __name__ == '__main__':
    s = input()

    if s[:3] == 'yah' and s[3] == s[4]:
        print('YES')
    else:
        print('NO')
