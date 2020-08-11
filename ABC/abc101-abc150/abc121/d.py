# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    start = a
    ans = a

    if a % 2 == 0:
        if b - (a - 1) >= 4:
            start = b - ((b - (a - 1)) % 4)
            ans = 0
    else:
        if b - a >= 4:
            start = b - ((b - a) % 4)
            ans = a

    for i in range(start + 1, b + 1):
        ans ^= i

    print(ans)


if __name__ == '__main__':
    main()
