# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate, pairwise

    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    size = 0
    size_max = 2 * 10**5 + 10
    sizes = [0] * size_max
    acc_sizes = [0] * size_max
    s = set()
    d = {i: [0] for i in range(1, n + 1)}

    for i, xi in enumerate(x, 1):
        if xi in s:
            s.discard(xi)
            size -= 1
        else:
            s.add(xi)
            size += 1

        sizes[i] += size

        d[xi].append(i)

    for i in range(1, n + 1):
        d[i].append(size_max - 1)

    acc_sizes = list(accumulate(sizes))
    minus = [0] * size_max

    for key, values in d.items():
        if len(values) == 2:
            continue

        for i, (first, second) in enumerate(pairwise(values)):
            if i % 2 == 1:
                continue

            if first != 0:
                first -= 1

            diff = acc_sizes[second - 1] - acc_sizes[first]
            minus[key] += diff

    total = acc_sizes[-1]
    ans = list()

    for i in range(1, n + 1):
        if len(d[i]) == 2:
            candidate = 0
        else:
            candidate = total - minus[i]

        ans.append(candidate)

    print(*ans)


if __name__ == "__main__":
    main()
