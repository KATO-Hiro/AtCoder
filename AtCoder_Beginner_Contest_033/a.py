# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    from collections import Counter

    for key, value in Counter(list(map(int, input()))).items():
        if value == 4:
            print('SAME')
            exit()

    print('DIFFERENT')
