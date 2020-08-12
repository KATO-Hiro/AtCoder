# -*- coding: utf-8 -*-


def main():
    t = input()
    words = ''

    for ti in t:
        if ti == '?':
            words += 'D'
        else:
            words += ti

    print(words)


if __name__ == '__main__':
    main()
