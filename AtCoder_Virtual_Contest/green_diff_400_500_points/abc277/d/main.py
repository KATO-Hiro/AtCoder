# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    prev = a[0]
    summed = a[0]
    candidates = list()

    for ai in a[1:]:
        if ai == prev or ai == ((prev + 1) % m):
            summed += ai
        else:
            candidates.append(summed)
            summed = ai

        prev = ai

    if summed > 0:
        candidates.append(summed)

    value_max = max(candidates)
    ans = sum(candidates) - value_max

    if a[0] == ((a[-1] + 1) % m) and len(candidates) >= 2:
        if candidates[0] == value_max:
            ans -= candidates[-1]
        elif candidates[-1] == value_max:
            ans -= candidates[0]

    # print(a)
    # print(candidates)
    print(ans)


if __name__ == "__main__":
    main()
