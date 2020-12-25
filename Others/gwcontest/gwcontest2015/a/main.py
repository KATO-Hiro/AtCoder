# -*- coding: utf-8 -*-


def main():
    from itertools import product

    scores1 = [25, 39, 51, 76, 163, 111, 136, 128, 133, 138]
    scores2 = [25, 39, 51, 76, 163, 111, 58, 128, 133, 138]
    total = set()

    for pattern in list(product([0, 1], repeat=10)):
        summed = 0

        for s, p in zip(scores1, pattern):
            summed += s * p

        total.add(summed)

        summed = 0

        for s, p in zip(scores2, pattern):
            summed += s * p

        total.add(summed)

    print("\n".join(map(str, sorted(total))))


if __name__ == "__main__":
    main()
