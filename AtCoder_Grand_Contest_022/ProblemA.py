'''input
abcdefghijklmnopqrstuvwzyx
abcdefghijklmnopqrstuvx

bacdefghijklmnopqrstuvwzyx
bacdefghijklmnopqrstuvx

atcoder
atcoderb

abc
abcd

zyxwvutsrqponmlkjihgfedcba
-1

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


# See:
# https://img.atcoder.jp/agc022/editorial.pdf
# https://agc022.contest.atcoder.jp/submissions/2286541
# https://docs.google.com/document/d/1cNq5-tBwMmuZ2qEfshXptpFxkFWK_3bgogr_MqDysuc/edit
def determine_next_word(given_word: str) -> str:
    while given_word:
        pi = ascii_lowercase.index(given_word[-1])
        given_word = given_word[:-1]

        for character in ascii_lowercase[pi + 1:]:
            if character not in given_word:
                return given_word + character


if __name__ == '__main__':
    from string import ascii_lowercase
    s = input()

    if len(s) < 26:
        result = [s + character for character in ascii_lowercase if character not in s][0]
        print(result)
    elif s == ascii_lowercase[::-1]:
        print(-1)
    else:
        print(determine_next_word(given_word=s))
