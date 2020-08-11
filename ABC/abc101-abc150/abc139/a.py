# -*- coding: utf-8 -*-


def main():
    s = input()
    t = input()
    count = 0

    for si, ti in zip(s, t):
        if si == ti:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
