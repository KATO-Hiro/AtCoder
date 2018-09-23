# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    s = sorted(Counter(list(input())).items(), key=lambda x: x[0])
    t = sorted(Counter(list(input())).items(), key=lambda x: x[0])
    diff_s = [0] * 26
    diff_t = [0] * 26
    alphabets = [chr(ord('a') + i) for i in range(26)]

    if len(s) == len(t):
        for alpha, count in s:
            if alpha in alphabets:
                diff_s[alphabets.index(alpha)] = count

        for alpha, count in t:
            if alpha in alphabets:
                diff_t[alphabets.index(alpha)] = count

        for si, ti in zip(sorted(diff_s), sorted(diff_t)):
            if si != ti:
                print('No')
                exit()

        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
