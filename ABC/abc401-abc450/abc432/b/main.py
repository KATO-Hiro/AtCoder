# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    x = list(input().rstrip())
    m = len(x)

    patterns = list(permutations(range(m)))
    candidates = list()

    for pattern in patterns:
        candidate = list()

        for pi in pattern:
            candidate += x[pi]

        if candidate[0] == "0":
            continue

        number = int("".join(candidate))
        candidates.append(number)

    print(min(candidates))


if __name__ == "__main__":
    main()
