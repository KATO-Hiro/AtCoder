# -*- coding: utf-8 -*-


def main():
    s = [c for c in input()]
    k = int(input())
    l = len(s)

    # See:
    # https://atcoder.jp/contests/code-festival-2016-quala/submissions/1033174
    for i in range(l):
        t = (ord('z') - ord(s[i]) + 1) % 26

        if t <= k:
            k -= t
            s[i] = 'a'

    s[-1] = chr((ord(s[-1]) - ord('a') + k) % 26 + ord('a'))

    print(''.join(s))


if __name__ == '__main__':
    main()
