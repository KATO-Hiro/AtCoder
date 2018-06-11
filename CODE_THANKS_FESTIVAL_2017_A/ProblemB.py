# -*- coding: utf-8 -*-
# CODE THANKS FESTIVAL 2017(Parallel)
# Problem B

if __name__ == '__main__':
    s = input()
    i = 0
    count = 0

    while len(s) > 0:
        if s[i:] == s[i:][::-1]:
            print(count)
            exit()
        else:
            i += 1
            count += 1
