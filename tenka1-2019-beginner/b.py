# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    k = int(input())
    ans = ''
    kth_s = s[k - 1]

    for si in s:
        if si != kth_s:
            ans += '*'
        else:
            ans += si

    print(ans)


if __name__ == '__main__':
    main()
