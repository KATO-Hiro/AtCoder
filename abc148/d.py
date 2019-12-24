# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    number = 1

    for ai in a:
        if ai == number:
            number += 1
        else:
            count += 1

    if count == n:
        print(-1)
    else:
        print(count)


if __name__ == '__main__':
    main()
