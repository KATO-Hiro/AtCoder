# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 1

    for ai in a:
        if ai == 1:
            print(count)
            exit()
        else:
            count += 1


if __name__ == '__main__':
    main()
