# -*- coding: utf-8 -*-


from bisect import bisect_left


def bisect_lt(sorted_array: list[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_ge(sorted_array: list[int], value: int):
    """Find the smallest element >= x and its index, or None if it doesn't exist."""

    if sorted_array[-1] >= value:
        index: int = bisect_left(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    s = input().rstrip()
    a_count, b_count = list(), list()

    for si in s:
        if si == "a":
            a_count.append(1)
            b_count.append(0)
        else:
            a_count.append(0)
            b_count.append(1)

    inf = 10**18
    a_count.append(inf)
    b_count.append(inf)

    acc_a = list(accumulate(a_count, initial=0))
    acc_b = list(accumulate(b_count, initial=0))
    ans = 0

    for k in range(n + 1):
        i, _ = bisect_ge(acc_a, acc_a[k] + a)
        j, _ = bisect_lt(acc_b, acc_b[k] + b)
        ans += max(0, j - i + 1)

    print(ans)


if __name__ == "__main__":
    main()
