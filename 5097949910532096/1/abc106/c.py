# -*- coding: utf-8 -*-


def main():
    s = input()
    k = int(input())
    count = 0

    for si in s:
        if si == '1':
            count += 1
        else:
            break

    if s[0] != '1':
        print(s[0])
    else:
        if k <= count:
            print(1)
        else:
            print(s[count])


if __name__ == '__main__':
    main()
