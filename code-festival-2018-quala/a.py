# -*- coding: utf-8 -*-


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    s = int(input())

    for i in range(4):
        if a + b + c + i == s:
            print('Yes')
            exit()

    print('No')


if __name__ == '__main__':
    main()
