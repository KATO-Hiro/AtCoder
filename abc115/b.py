# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = sorted([int(input()) for _ in range(n)])
    ans = 0

    for index, pi in enumerate(p, 1):
        if index == n:
            ans += int(pi / 2)
        else:
            ans += pi

    print(ans)


if __name__ == '__main__':
    main()
