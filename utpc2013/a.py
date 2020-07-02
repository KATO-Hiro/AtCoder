# -*- coding: utf-8 -*-


def main():
    s = input()

    one = ['A', 'D', 'O', 'P', 'Q', 'R']
    two = ['B']

    for index, si in enumerate(s):
        if index == 2 and si not in one:
            print('no')
            exit()

        if si in one and si in two:
            print('no')
            exit()

    print('yes')


if __name__ == '__main__':
    main()
