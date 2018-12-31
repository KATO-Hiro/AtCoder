# -*- coding: utf-8 -*-


def main():
    s = input()
    count = 0

    while count < 1500:
        s = s.replace('25', '')
        count += 1

        if len(s) == 0:
            print(count)
            exit()

    print(-1)


if __name__ == '__main__':
    main()
