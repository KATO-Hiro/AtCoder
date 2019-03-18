# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for _ in range(n + 1)]

    # See:
    # https://www.slideshare.net/chokudai/codefestival2015quala
    for i in range(n):
        ans[i + 1] = 2 * ans[i] + a[i]

    print(ans[n])


if __name__ == '__main__':
    main()
