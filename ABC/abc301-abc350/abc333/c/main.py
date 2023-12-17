# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n -= 1
    repunits = [1]

    for _ in range(15):
        value = repunits[-1] * 10 + 1
        repunits.append(value)

    candidates = set()

    for v1 in repunits:
        for v2 in repunits:
            for v3 in repunits:
                candidates.add(v1 + v2 + v3)

    candidates = sorted(candidates)
    print(candidates[n])


if __name__ == "__main__":
    main()
