# -*- coding: utf-8 -*-
# CODE THANKS FESTIVAL 2017(Parallel)
# Problem B

if __name__ == '__main__':
    s = input()

    if s == s[::-1]:
        print(0)
    else:
        i = 0
        count = 0

        while len(s) > 0:
            mod_s = s[i:]

            if mod_s == mod_s[::-1]:
                print(count)
                exit()
            else:
                i += 1
                count += 1
