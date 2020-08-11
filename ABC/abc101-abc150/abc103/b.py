# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input()
    t = input()
    mod_s = s

    for i in range(len(s)):
        mod_s = mod_s[1:] + mod_s[0]

        if mod_s == t:
            print('Yes')
            exit()

    print('No')
