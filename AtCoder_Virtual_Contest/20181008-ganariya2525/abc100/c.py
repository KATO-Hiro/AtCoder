# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for ai in a:
        while ai % 2 == 0:
            ans += 1
            ai = ai // 2

    print(ans)


if __name__ == '__main__':
    main()
