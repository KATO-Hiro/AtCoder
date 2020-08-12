# -*- coding: utf-8 -*-


def main():
    a, b, k = map(int, input().split())
    takahashi = a
    aoki = b

    for i in range(k):
        if i % 2 == 0:
            if takahashi % 2 == 1:
                takahashi -= 1

            takahashi -= takahashi // 2
            aoki += takahashi
        else:
            if aoki % 2 == 1:
                aoki -= 1

            aoki -= aoki // 2
            takahashi += aoki

    print(takahashi, aoki)


if __name__ == '__main__':
    main()
