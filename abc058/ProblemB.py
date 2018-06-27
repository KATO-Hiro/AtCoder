'''input
xy
abc
xaybc

xyz
abc
xaybzc

atcoderbeginnercontest
atcoderregularcontest
aattccooddeerrbreeggiunlnaerrccoonntteesstt

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    odd_th_password = input()
    even_th_password = input()
    original_password = ''

    for i in range(max(len(odd_th_password), len(even_th_password))):
        if i < len(odd_th_password):
            original_password += ''.join(odd_th_password[i])
        if i < len(even_th_password):
            original_password += ''.join(even_th_password[i])

    print(original_password)
