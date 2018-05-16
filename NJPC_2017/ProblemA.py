'''input
37
narasenntannkagakugijyutudaigakuinndaigaku
narasenntannkagakugijyutudaigakuinnda

10
hello
hello

'''

# -*- coding: utf-8 -*-

# NJPC 2017
# Problem A

if __name__ == '__main__':
    lengeth = int(input())
    s = input()

    if len(s) > lengeth:
        print(s[:lengeth])
    else:
        print(s)
