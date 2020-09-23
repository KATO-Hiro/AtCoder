# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    first = list()
    second = list()
    third = list()
    ans = [0 for _ in range(n)]

    for i in range(n):
        f, s, t = map(int, input().split())
        first.append(f)
        second.append(s)
        third.append(t)

    for index, fi in enumerate(first):
        if first.count(fi) == 1:
            ans[index] += fi

    for index, se in enumerate(second):
        if second.count(se) == 1:
            ans[index] += se

    for index, th in enumerate(third):
        if third.count(th) == 1:
            ans[index] += th

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
