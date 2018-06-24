# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


# See:
# http://terukizm.hatenablog.com/entry/20120505/1336218368
def ceil(src, range):
    return ((int)(src / range) + 1) * range


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    tmp = (n - 1) % (k - 1)

    if tmp == 0:
        print((n - 1) // (k - 1))
    else:
        print(ceil((n - 1) / (k - 1), 1))
