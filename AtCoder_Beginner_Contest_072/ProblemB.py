'''input
fukuokayamaguchi
fkoaaauh

atcoder
acdr

aaaa
aa

z
z

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    s = list(str(input()))
    result = s[::2]
    print(''.join(result))
