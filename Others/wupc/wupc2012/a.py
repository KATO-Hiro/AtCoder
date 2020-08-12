# -*- coding: utf-8 -*-


def main():
    from datetime import datetime

    ma, da = map(str, input().split())
    mb, db = map(str, input().split())
    start = '2012/' + ma + '/' + da
    finish = '2012/' + mb + '/' + db
    diff = datetime.strptime(finish, '%Y/%m/%d') - datetime.strptime(start, '%Y/%m/%d')

    print(diff.days)


if __name__ == '__main__':
    main()
