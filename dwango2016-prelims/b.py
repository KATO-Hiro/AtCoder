# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    k = list(map(int, input().split()))
    ans = [k[0]]

    for i, j in zip(k, k[1:]):
        ans.append(min(i, j))

    ans.append(k[-1])
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
