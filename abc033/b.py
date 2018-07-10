'''input
14
yasuzuka 3340
uragawara 4032
oshima 2249
maki 2614
kakizaki 11484
ogata 10401
kubiki 9746
yoshikawa 5142
joetsu 100000
nakago 4733
itakura 7517
kiyosato 3152
sanwa 6190
nadachi 3169
joetsu

4
unagi 20
usagi 13
snuke 42
smeke 7
snuke

5
a 10
b 20
c 30
d 40
e 101
e

5
a 10
b 20
c 30
d 40
e 100
atcoder

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    from math import ceil
    n = int(input())
    total_population = 0
    sp = dict()

    for i in range(n):
        s, p = list(map(str, input().split()))
        total_population += int(p)
        sp[s] = int(p)

    candidate_name = sorted(sp.items(), key=lambda x: x[1], reverse=True)[0]

    if candidate_name[1] > ceil(total_population // 2):
        print(candidate_name[0])
    else:
        print('atcoder')
