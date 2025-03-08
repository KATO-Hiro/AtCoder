# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter
    from itertools import combinations

    input = sys.stdin.readline

    n = int(input())
    x = input().rstrip()
    y = list(combinations(x, 3))

    def f(i, s):
        c = Counter(s)
        value_max = max(c.values())
        results = [(value, key, i) for key, value in c.items() if value == value_max]
        results.sort()

        return results[0]

    candidate = list()

    for i in range(1, n + 1):
        si = input().rstrip()
        t = list(combinations(si, 2))

        tmp = set()

        for yi in y:
            for ti in t:
                ui = yi + ti
                result = f(i, ui)
                tmp.add(result)

        tmp = sorted(tmp, key=lambda x: (-x[0], x[1]))
        candidate.append(tmp[0])

    ans = list()

    for i in range(n):
        win_count = 0

        for j in range(n):
            if i == j:
                continue

            count_i, alpha_i, id_i = candidate[i]
            count_j, alpha_j, id_j = candidate[j]

            if count_i > count_j:
                win_count += 1
            elif count_i == count_j:
                if alpha_i < alpha_j:
                    win_count += 1
                elif alpha_i == alpha_j:
                    if id_i < id_j:
                        win_count += 1

        ans.append((win_count, i + 1))

    ans = sorted(ans, key=lambda x: (-x[0], x[1]))
    print(ans[0][1])


if __name__ == "__main__":
    main()
