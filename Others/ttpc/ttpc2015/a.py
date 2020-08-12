# -*- coding: utf-8 -*-


def main():
    s = input()
    year = s[:2]
    grade = s[2]

    if grade == 'B':
        print('Bachelor', year)
    elif grade == 'M':
        print('Master', year)
    else:
        print('Doctor', year)


if __name__ == '__main__':
    main()
