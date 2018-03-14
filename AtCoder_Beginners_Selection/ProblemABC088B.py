'''input
4
20 18 2 18
18
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    card_count = int(input())
    cards = list(map(int, input().split()))

    sorted_cards = sorted(cards, reverse=True)

    alice_point = sum(sorted_cards[::2])
    bob_point = sum(sorted_cards[1::2])

    diff = alice_point - bob_point
    print(diff)
