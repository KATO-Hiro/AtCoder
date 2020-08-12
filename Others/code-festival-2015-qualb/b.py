# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n, m = map(int, input().split())
    a = Counter(list(map(int, input().split())))
    ans = a.most_common(1)

    if ans[0][1] >= (n // 2 + 1):
        print(ans[0][0])
    else:
        print('?')


if __name__ == '__main__':
    main()
