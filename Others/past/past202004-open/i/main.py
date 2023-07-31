# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    m = n
    a = list(map(int, input().split()))
    c = a.copy()
    results = defaultdict(list)
    round = 1

    while n > 0:
        if n == 1:
            results[round].append(a[0])
            results[round].append(a[1])
        else:
            b = list()

            for i in range(2 ** (n - 1)):
                first, second = a[2 * i], a[2 * i + 1]

                if first > second:
                    results[round].append(second)
                    b.append(first)
                else:
                    results[round].append(first)
                    b.append(second)

            a = b

        round += 1
        n -= 1

    ans = [-1] * (2**m)

    for key, values in results.items():
        for value in values:
            # print(c.index(value))
            ans[c.index(value)] = key

    # print(results)
    # print(c)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
