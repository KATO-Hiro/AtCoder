# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [input() for _ in range(5)]
    zero = ['###', '#.#', '#.#', '#.#', '###']
    one = ['.#.', '##.', '.#.', '.#.', '###']
    two = ['###', '..#', '###', '#..', '###']
    three = ['###', '..#', '###', '..#', '###']
    four = ['#.#', '#.#', '###', '..#', '..#']
    five = ['###', '#..', '###', '..#', '###']
    six = ['###', '#..', '###', '#.#', '###']
    seven = ['###', '..#', '..#', '..#', '..#']
    eight = ['###', '#.#', '###', '#.#', '###']
    nine = ['###', '#.#', '###', '..#', '###']
    numbers = {'0': zero, '1': one, '2': two, '3': three,
               '4': four, '5': five, '6': six,
               '7': seven, '8': eight, '9': nine
               }
    ans = ''

    for i in range(n):
        for key, value in numbers.items():
            count = 0

            for si, v in zip(s, value):
                sub_si = si[4 * i + 1: 4 * i + 4]

                if sub_si == v:
                    count += 1

            if count == 5:
                ans += key

    print(ans)


if __name__ == '__main__':
    main()
