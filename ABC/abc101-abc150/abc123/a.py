# -*- coding: utf-8 -*-


def main():
    alpha = [int(input()) for _ in range(5)]
    k = int(input())

    for a in alpha:
        for b in alpha:
            if abs(a - b) > k:
                print(':(')
                exit()

    print('Yay!')


if __name__ == '__main__':
    main()
