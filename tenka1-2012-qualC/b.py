# -*- coding: utf-8 -*-


def main():
    s = input()
    cards = list()
    sub_s = ''
    marks = ['S', 'H', 'D', 'C']
    numbers = ['10', 'J', 'Q', 'K', 'A']

    for si in s:
        if si in marks:
            if sub_s != '':
                cards.append(sub_s)

            sub_s = si
        else:
            sub_s += si

    ans = 'x' * (10 ** 5)

    for mark in marks:
        comb = list()
        candidate = ''

        for number in numbers:
            comb.append(mark + number)

        count = 0

        for card in cards:
            if count == 5:
                continue

            if card in comb:
                count += 1
            else:
                candidate += card

        if len(ans) > len(candidate):
            ans = candidate

    if ans == '':
        ans = '0'

    print(ans)


if __name__ == '__main__':
    main()
