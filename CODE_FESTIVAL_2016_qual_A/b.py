# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    # See:
    # http://code-festival-2016-quala.contest.atcoder.jp/data/other/code-festival-2016-quala/editorial.pdf
    for i in range(len(a)):
        if i == a[a[i] - 1] - 1:
            count += 1

    print(count // 2)
