# -*- coding: utf-8 -*-


def main():
    a, b, x = map(int, input().split())

    digit = len(list(str(x // a)))
    ans = 0

    for d in range(digit, 0, -1):
        candidate = (x - b * d) // a
        candidate = min(candidate, 10 ** 9)
        candidate = max(0, candidate)

        if a * candidate + b * len(list(str(candidate))) <= x:
            ans = max(ans, candidate)

    print(ans)


if __name__ == '__main__':
    main()
