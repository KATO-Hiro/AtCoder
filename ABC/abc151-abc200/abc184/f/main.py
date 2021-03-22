# -*- coding: utf-8 -*-


def generate_patterns(elements, bound):
    results = [0]
    size = len(elements)

    for bit in range(1, 1 << size):
        summed = 0

        for i in range(size):
            if bit & (1 << i):
                summed += elements[i]

        if summed <= bound:
            results.append(summed)

    return results


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        exit()

    mid = n // 2
    first = a[:mid]
    second = a[mid:]
    ans = 0

    first_patterns = generate_patterns(first, t)
    second_patterns = sorted([0] + generate_patterns(second, t))

    left_index = 0
    right_index = len(second_patterns)

    for first_pattern in first_patterns:
        remain = t - first_pattern

        if remain > second_patterns[-1]:
            remain = second_patterns[-1]

        left = left_index
        right = right_index

        while (right - left) > 1:
            mid = (left + right) // 2

            if second_patterns[mid] > remain:
                right = mid
            else:
                left = mid

        ans = max(ans, first_pattern + second_patterns[left])

    print(ans)


if __name__ == "__main__":
    main()
