# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    minus_count = 0
    abs_min = float('inf')
    ans = 0

    for ai in a:
        if ai < 0:
            minus_count += 1

        abs_min = min(abs_min, abs(ai))
        ans += abs(ai)

    if minus_count % 2 == 1:
        ans -= abs_min * 2

    print(ans)


if __name__ == '__main__':
    main()
