# -*- coding: utf-8 -*-


def main():
    s = input()
    ans = ''

    for si in s:
        if si == '0':
            ans += si
        elif si == '1':
            ans += si
        elif si == 'B' and len(ans) == 0:
            pass
        elif si == 'B' and len(ans) > 0:
            ans = ans[:len(ans) - 1]

    print(ans)


if __name__ == '__main__':
    main()
