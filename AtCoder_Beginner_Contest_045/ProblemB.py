'''input
aca
accc
ca
A

abcb
aacb
bccc
C

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    a_cards = list(input())
    b_cards = list(input())
    c_cards = list(input())
    current_card = a_cards.pop(0)

    while True:
        if current_card == 'a':
            if len(a_cards) == 0:
                print(current_card.upper())
                exit()

            current_card = a_cards.pop(0)

        elif current_card == 'b':
            if len(b_cards) == 0:
                print(current_card.upper())
                exit()

            current_card = b_cards.pop(0)

        elif current_card == 'c':
            if len(c_cards) == 0:
                print(current_card.upper())
                exit()

            current_card = c_cards.pop(0)
