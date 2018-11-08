# -*- coding: utf-8 -*-


def main():
    from itertools import combinations

    five_numbers = list(map(int, input().split()))
    summed_five_numbers = list()

    for first, second, third in list(combinations(five_numbers, 3)):
        summed_five_numbers.append(first + second + third)

    print(sorted(summed_five_numbers, reverse=True)[2])


if __name__ == '__main__':
    main()
