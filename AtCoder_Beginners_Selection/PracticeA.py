'''input
1
2 3
test
'''

# -*- coding: utf-8 -*-
a = int(input())
b, c = list(map(int, input().split()))
s = input()

print(str(a + b + c) + " " + s)
