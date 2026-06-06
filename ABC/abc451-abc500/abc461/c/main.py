# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k, m = map(int, input().split())
    pending = -1
    c_max = [pending] * n
    d = defaultdict(list)

    for _ in range(n):
        ci, vi = map(int, input().split())
        ci -= 1

        d[ci].append(vi)
        c_max[ci] = max(c_max[ci], vi)

    candidates = []

    for i, c_max_i in enumerate(c_max):
        if c_max_i == pending:
            continue

        candidates.append(c_max_i)

    candidates.sort(reverse=True)

    remains = []

    while len(candidates) > m:
        remains.append(candidates.pop())

    for key, values in d.items():
        values = sorted(values)
        values.pop()

        remains += values

    remains.sort()

    while len(candidates) < k:
        value = remains.pop()
        candidates.append(value)

    ans = sum(candidates)
    print(ans)


if __name__ == "__main__":
    main()
