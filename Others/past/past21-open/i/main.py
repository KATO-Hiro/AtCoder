# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = defaultdict(int)
    numbers = set()

    for i in range(k):
        freq[a[i]] += 1
        numbers.add(a[i])

    ans = 0

    if len(numbers) == k:
        ans += 1

    for i in range(1, n):
        ni = i + k - 1

        if ni >= n:
            break

        prev = a[i - 1]
        freq[prev] -= 1

        if freq[prev] == 0:
            numbers.discard(prev)

        next = a[ni]

        if freq[next] == 0:
            numbers.add(next)

        freq[next] += 1

        if len(numbers) == k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
