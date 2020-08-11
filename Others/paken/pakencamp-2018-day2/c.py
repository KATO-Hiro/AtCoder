# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    a = list(map(int, input().split()))

    for p in range(n):
        count = 0

        for pi in range(p):
            keys = Counter(a[pi::p]).keys()

            if len(keys) == 1 or (len(keys) == 2 and 0 in keys):
                count += 1

        if p > 0 and count == p:
            print(p)
            exit()

    print(len(a))


if __name__ == '__main__':
    main()
