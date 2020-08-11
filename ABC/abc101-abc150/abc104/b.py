# -*- coding: utf-8 -*-


def main():
    s = input()
    c_count = 0
    s0 = s[0]

    for i in range(2, len(s) - 1):
        if s[i] == 'C':
            c_count += 1

    s = s.replace('A', '', 1)
    s = s.replace('C', '', 1)
    result = s.islower()

    if s0 == 'A' and c_count == 1 and result is True:
        print('AC')
    else:
        print('WA')


if __name__ == '__main__':
    main()
