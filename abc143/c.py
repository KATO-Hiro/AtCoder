# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    prev = s[0]
    count = 1

    for i in range(1, n):
        cur = s[i]

        if cur != prev:
            count += 1
            prev = cur

    print(count)


if __name__ == '__main__':
    main()
