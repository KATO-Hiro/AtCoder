# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()

    if n % 2 == 1:
        print(-1)
    else:
        count = 0

        for former, latter in zip(s[:n // 2], s[n // 2:]):
            if former != latter:
                count += 1

        print(count)


if __name__ == '__main__':
    main()
