# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys
    input = sys.stdin.readline

    n = int(input())
    k = int(input())
    number = [int(input()) for _ in range(n)]
    ans = set()

    for cards in list(permutations(number, k)):
        card_number = ''

        for card in cards:
            card_number += str(card)

        ans.add(card_number)

    print(len(ans))


if __name__ == '__main__':
    main()
