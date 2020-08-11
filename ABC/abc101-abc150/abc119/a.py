# -*- coding: utf-8 -*-


def main():
    from datetime import datetime

    s = input()

    if datetime.strptime(s, '%Y/%m/%d') <= datetime(2019, 4, 30):
        print('Heisei')
    else:
        print('TBD')


if __name__ == '__main__':
    main()
