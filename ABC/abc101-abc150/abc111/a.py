# -*- coding: utf-8 -*-


def main():
    s = input()
    mod = ''

    for i in range(3):
        if s[i] == '1':
            mod += '9'
        elif s[i] == '9':
            mod += '1'

    print(mod)


if __name__ == '__main__':
    main()
