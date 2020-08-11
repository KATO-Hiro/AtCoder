# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    s = input()
    t = input()
    ans = 0

    for si, ti in zip(s, t):
        if si != ti:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
