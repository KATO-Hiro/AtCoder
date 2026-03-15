from bisect import bisect_right
from typing import List


def bisect_le(sorted_array: List[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def main():
    import sys
    from collections import defaultdict
    from string import ascii_lowercase

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    l -= 1
    s = input().rstrip()
    inf = 10**9
    d = defaultdict(list)

    for i, si in enumerate(s):
        if si not in d:
            d[si] = [-inf]

        d[si].append(i)

    for alpha in ascii_lowercase:
        if alpha in d:
            d[alpha].append(inf)

    ans = 0

    for values in d.values():
        for value in values:
            if value == -inf or value == inf:
                continue

            j, _ = bisect_le(values, value + r)
            i, _ = bisect_le(values, value + l)

            ans += j - i

    print(ans)


if __name__ == "__main__":
    main()
