# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        if 10 <= i <= 99:
            continue
        elif 1000 <= i <= 9999:
            continue
        elif i == 100000:
            continue
        else:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
