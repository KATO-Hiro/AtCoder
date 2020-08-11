# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = 1

    for i in range(1, n + 1):
        ans += 5 ** i

    print(ans)


if __name__ == '__main__':
    main()
