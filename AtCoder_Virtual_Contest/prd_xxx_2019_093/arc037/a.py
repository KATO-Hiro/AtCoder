# -*- coding: utf-8 -*-


def main():
    n = int(input())
    m = list(map(int, input().split()))
    ans = 0

    for mi in m:
        if mi < 80:
            ans += 80 - mi

    print(ans)


if __name__ == '__main__':
    main()
