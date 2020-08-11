# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    count = 0

    for ai in a:
        if ai == 0:
            count = 0
        elif ai == 1:
            count += 1

        ans = max(ans, count)

    print(ans + 1)


if __name__ == '__main__':
    main()
