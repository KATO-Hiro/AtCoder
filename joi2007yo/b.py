# -*- coding: utf-8 -*-


def main():
    numbers = dict()

    for i in range(1, 31):
        numbers[i] = 0

    for k in range(28):
        submit_number = int(input())
        numbers[submit_number] = 1

    for number, count in numbers.items():
        if count == 0:
            print(number)


if __name__ == '__main__':
    main()
