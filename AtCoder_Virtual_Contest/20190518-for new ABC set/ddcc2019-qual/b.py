# -*- coding: utf-8 -*-


def main():
    n = int(input())
    added = 0
    ans = 0

    if n % 2 == 1:
        ans += 1

    for i in range((max(0, n - 2) // 2)):
        added += 4
        ans += added

    print(ans)


if __name__ == '__main__':
    main()
