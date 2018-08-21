# -*- coding: utf-8 -*-


def main():
    s = input()
    t = s[::-1]

    # See:
    # https://www.slideshare.net/chokudai/arc035
    for si, ti in zip(s, t):
        if (si == ti):
            pass
        elif (si == '*') or (ti == '*'):
            pass
        else:
            print('NO')
            exit()

    print('YES')


if __name__ == '__main__':
    main()
