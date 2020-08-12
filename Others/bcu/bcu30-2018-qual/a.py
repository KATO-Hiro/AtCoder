# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for _ in range(30)]

    for ai in a:
        ans[ai] += 1

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
