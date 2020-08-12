# -*- coding: utf-8 -*-


def main():
    s = input().split()
    m = len(s)
    ans = ['' for _ in range(m)]
    n = int(input())

    for i in range(n):
        ti = input()
        ti_count = len(ti)

        for index, si in enumerate(s):
            si_count = len(si)

            if si_count != ti_count:
                continue

            count = 0

            for sii, tii in zip(si, ti):
                if sii == tii:
                    count += 1
                if tii == '*':
                    count += 1

            if count == ti_count:
                ans[index] = '*' * count

    for index, a in enumerate(ans):
        if a == '':
            ans[index] = s[index]

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
