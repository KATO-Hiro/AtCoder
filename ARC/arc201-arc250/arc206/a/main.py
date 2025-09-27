# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    freq = defaultdict(int)
    ans = 1

    for i in range(n - 1, -1, -1):
        if i < n - 1 and a[i] != a[i + 1]:
            ans += n - (i + 1)
            ans -= freq[a[i]]

        freq[a[i]] += 1

    print(ans)


if __name__ == "__main__":
    main()
