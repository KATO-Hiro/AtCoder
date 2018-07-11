# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    s = input()
    k = int(input())
    passwords = set()

    if k > len(s):
        print(0)
        exit()

    for i in range(len(s) - k + 1):
        passwords.add(s[i:i + k])

    print(len(passwords))
