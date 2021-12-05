# -*- coding: utf-8 -*-


def main():
    s = input()
    t1 = 'oxx' * 4
    t2 = 'xxo' * 4
    t3 = 'xox' * 4

    if s in t1 or s in t2 or s in t3:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
