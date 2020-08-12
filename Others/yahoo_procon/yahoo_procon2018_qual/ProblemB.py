'''input
100 7
10000000

2018 2
2100

888 0
889

'''

# -*- coding: utf-8 -*-

# yahoo procon2018 qual
# Problem B


# See:
# http://terukizm.hatenablog.com/entry/20120505/1336218368
def ceil(src, range):
    return ((int)(src / range) + 1) * range


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(ceil(n, 10 ** k))
