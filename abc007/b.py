# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase

    a = input()
    a_len = len(a)

    if a_len >= 2:
        print(a[:a_len - 1])
    else:
        alpha = ascii_lowercase
        index = alpha.index(a)

        if index == 0:
            print('-1')
        else:
            print(alpha[index - 1])


if __name__ == '__main__':
    main()
