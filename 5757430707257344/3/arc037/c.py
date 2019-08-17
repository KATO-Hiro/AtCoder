# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = list()

    for ai in a:
        for bi in b:
            ans.append(ai * bi)

    print(sorted(ans)[k - 1])


if __name__ == '__main__':
    main()
