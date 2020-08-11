'''input
oxo
900

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    s = input()
    added = s.count('o')

    print(700 + int(added) * 100)
