'''input
6
red
red
blue
yellow
yellow
red
5
red
red
yellow
green
blue

1
1
voldemort
10
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort

0
3
apple
orange
apple
5
apple
apple
apple
apple
apple

1


6
red
red
blue
yellow
yellow
red
5
red
red
yellow
green
blue

1

3
apple
orange
apple
1
grape

2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    blue_card_count = int(input())
    blue_cards = list()

    for i in range(blue_card_count):
        blue_cards.append(input())

    red_card_count = int(input())
    red_cards = list()

    for i in range(red_card_count):
        red_cards.append(input())

    count_max = 0

    set_blue_card = set(blue_cards)

    for blue_card in set_blue_card:
        candidate = blue_cards.count(blue_card) - red_cards.count(blue_card)
        if candidate > count_max:
            count_max = candidate

    print(count_max)
