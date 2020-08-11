# -*- coding: utf-8 -*-


def count_rewrite_times(n, v, even, odd):
    ans = 0

    for x in range(n):
        if x % 2 == 0:
            if v[x] != even:
                ans += 1
        else:
            if v[x] != odd:
                ans += 1

    return ans


def main():
    from collections import Counter

    n = int(input())
    v = list(map(int, input().split()))

    if len(set(v)) == 1:
        print(n // 2)
        exit()
    else:
        even = Counter(v[::2]).most_common(1)[0][0]
        odd = Counter(v[1::2]).most_common(1)[0][0]

        if even == odd:
            even2 = Counter(v[::2]).most_common(2)[1][0]
            odd2 = Counter(v[1::2]).most_common(2)[1][0]

            print(min(count_rewrite_times(n, v, even, odd2),
                      count_rewrite_times(n, v, even2, odd)))
            exit()

        print(count_rewrite_times(n, v, even, odd))


if __name__ == '__main__':
    main()
