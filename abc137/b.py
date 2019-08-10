# -*- coding: utf-8 -*-


def main():
    k, x = map(int, input().split())
    ans = list()

    for i in range(max(-10 ** 6, x - k + 1), min(10 ** 6 + 1, k + x)):
        ans.append(i)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
