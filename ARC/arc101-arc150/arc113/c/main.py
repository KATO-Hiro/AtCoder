# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    freq = defaultdict(int)
    ans = 0

    for i in range(n - 1, -1, -1):
        freq[s[i]] += 1

        if i > n - 3:
            continue
        if s[i] != s[i + 1]:
            continue

        si = s[i]
        total = 0

        for cj, count in freq.items():
            if cj == si:
                continue

            total += count
            freq[cj] = 0

        ans += total
        freq[si] += total

    print(ans)


if __name__ == "__main__":
    main()
