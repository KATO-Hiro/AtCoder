# -*- coding: utf-8 -*-


def main():
    s = input().split(' ')
    n = len(s)
    ans = ''

    for i, si in enumerate(s):
        if si == '':
            pass
        elif i < n - 1:
            ans += si + ','
        elif i == n - 1:
            ans += si

    print(ans)


if __name__ == '__main__':
    main()
