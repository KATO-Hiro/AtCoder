'''input
aa

akasakaakasakasakaakas
14

abaababaab
6

xxxx
2

abcabcabcabc
6

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    s = input()
    ss = False

    while ss is False:
        s = s[:-1]
        boundary = int(len(s) / 2)
        forward = s[:boundary]
        backward = s[boundary:]

        if forward == backward:
            print(len(forward * 2))
            ss = True
