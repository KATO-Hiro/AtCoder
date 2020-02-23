# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))

    for ai in a:
        if ai % 2 == 0:
            if (ai % 3 == 0) or (ai % 5 == 0):
                pass
            else:
                print('DENIED')
                exit()

    print('APPROVED')


if __name__ == '__main__':
    main()
