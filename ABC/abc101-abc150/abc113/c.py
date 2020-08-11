# -*- coding: utf-8 -*-


def main():
    from collections import OrderedDict

    n, m = map(int, input().split())
    d = OrderedDict()
    ans = OrderedDict()

    for i in range(m):
        d[i] = tuple(map(int, input().split()))

    prev_pref = 0
    order = 1

    for key, value in sorted(d.items(), key=lambda x: x[1]):
        pref, year = value

        if pref == prev_pref:
            order += 1
        else:
            prev_pref = pref
            order = 1

        ans[key] = '{:0=6}'.format(pref) + '{:0=6}'.format(order)

    for key, value in sorted(ans.items(), key=lambda x: x[0]):
        print(value)


if __name__ == '__main__':
    main()
