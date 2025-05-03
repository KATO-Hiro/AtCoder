# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    n3 = 3 * n
    inf = 10**18

    def rec(used, value_max, value_min):
        if used == (1 << n3) - 1:
            return value_max - value_min

        result = inf

        # グループの所属していない人のうち、最もidが小さい人を選ぶ
        first = 0

        for j in range(n3):
            if (used >> j) & 1:
                continue

            first = j
            break

        # グループの所属していない人のうち、2人目・3人目を選ぶ
        for second in range(first + 1, n3):
            if (used >> second) & 1:
                continue

            for third in range(second + 1, n3):
                if (used >> third) & 1:
                    continue

                value_sum = a[first] + a[second] + a[third]
                new_used = used | (1 << first) | (1 << second) | (1 << third)

                candidate = rec(
                    used=new_used,
                    value_max=max(value_max, value_sum),
                    value_min=min(value_min, value_sum),
                )
                result = min(result, candidate)

        return result

    ans = rec(0, 0, inf)
    print(ans)


if __name__ == "__main__":
    main()
