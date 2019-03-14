# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    four_count = 0
    two_count = 0

    for ai in a:
        if ai % 4 == 0:
            four_count += 1
        elif ai % 2 == 0:
            two_count += 1

    if four_count >= n // 2:
        print('Yes')
    else:
        need = n - 2 * four_count

        if two_count >= need:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
