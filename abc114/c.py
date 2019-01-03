# -*- coding: utf-8 -*-


def main():
    from itertools import product

    n = int(input())
    numbers = list()
    ans = 0

    for digit in range(1, 10):
        for i in list(product(['3', '5', '7'], repeat=digit)):
            numbers.append(''.join(map(str, list(i))))

    for number in numbers:
        if int(number) <= n:
            if '3' in number and '5' in number and '7' in number:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
