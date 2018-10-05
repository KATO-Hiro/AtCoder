# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    like_numbers = [9, 7, 3, 1]
    count = 0

    for ai in a:
        for like_number in like_numbers:
            if ai >= like_number:
                count += ai - like_number
                break

    print(count)


if __name__ == '__main__':
    main()
