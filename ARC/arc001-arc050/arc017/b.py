# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    ans = 0
    increment_count = 0
    prev_a = 0

    # See:
    # https://www.slideshare.net/chokudai/arc017
    # https://beta.atcoder.jp/contests/arc017/submissions/1591520
    for i in range(n):
        if a[i] > prev_a:
            increment_count += 1
        else:
            increment_count = 1

        if increment_count >= k:
            ans += 1

        prev_a = a[i]

    print(ans)


if __name__ == '__main__':
    main()
