# -*- coding: utf-8 -*-


def main():
    s = int(input())
    a = list()
    a.append(s)
    i = 0

    while True:
        if a[i] % 2 == 0:
            tmp = a[i] // 2
        else:
            tmp = 3 * a[i] + 1

        i += 1

        if tmp in a:
            print(i + 1)
            exit()

        a.append(tmp)


if __name__ == '__main__':
    main()
