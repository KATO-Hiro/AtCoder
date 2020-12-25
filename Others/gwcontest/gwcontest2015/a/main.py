# -*- coding: utf-8 -*-


def main():
    from itertools import product

    scores = [25, 39, 51, 76, 163, 111, 128, 133, 138]
    g = [0, 58, 136]
    total = set()

    for pattern in list(product([0, 1], repeat=9)):
        summed = 0

        for s, p in zip(scores, pattern):
            summed += s * p

        for gi in g:
            total.add(summed + gi)

    print("\n".join(map(str, sorted(total))))


if __name__ == "__main__":
    main()
