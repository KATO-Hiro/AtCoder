# -*- coding: utf-8 -*-


from itertools import groupby


# See:
# https://qiita.com/Kept1994/items/e9179d1dd7c6455d6883
# RUN LENGTH ENCODING str -> st
def runLength_encode(s: str):
    grouped = groupby(s)
    res = ''

    for k, v in grouped:
        res += str(len(list(v)))
        res += str(k)

    return res


def main():
    n = int(input())
    s = input()

    for i in range(n):
        s = runLength_encode(s)

    print(s)


if __name__ == '__main__':
    main()
