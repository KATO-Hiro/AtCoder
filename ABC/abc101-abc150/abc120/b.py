# -*- coding: utf-8 -*-


def main():
    a, b, k = map(int, input().split())
    ans = list()

    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans.append(i)

    print(sorted(ans, reverse=True)[k - 1])


if __name__ == '__main__':
    main()
