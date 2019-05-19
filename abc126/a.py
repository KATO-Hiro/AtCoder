# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    s = input()
    ans = ''

    for i, si in enumerate(s):
        if i == k - 1:
            ans += si.lower()
        else:
            ans += si

    print(ans)


if __name__ == '__main__':
    main()
