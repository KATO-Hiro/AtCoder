# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    k = int(input())

    if k > n:
        print(0)
    else:
        ans = set()

        for i in range(n - k + 1):
            ans.add(s[i:i + k])

        print(len(ans))


if __name__ == '__main__':
    main()
