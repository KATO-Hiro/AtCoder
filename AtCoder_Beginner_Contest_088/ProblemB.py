# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    card_count = int(input())

    card_numbers = [int(i) for i in input().split()]
    card_numbers.sort(reverse=True)

    alice_score = 0
    bob_score = 0

    alice_cards = card_numbers[::2]
    bob_cards = card_numbers[1::2]

    for i in range(len(alice_cards)):
        alice_score += alice_cards[i]

    for j in range(len(bob_cards)):
        bob_score += bob_cards[j]

    diff = alice_score - bob_score
    print(diff)
