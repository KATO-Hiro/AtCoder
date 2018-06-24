# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    s = input()
    plus = s.count('+')
    minus = s.count('-') * -1
    print(plus + minus)
