# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = n // 2

    if n % 2 == 1:
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
