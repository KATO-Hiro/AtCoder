# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    scores = list(map(int, input().split()))
    ans = []

    for pattern in product([0, 1], repeat=5):
        user = ""
        summed_score = 0

        for pi, name, score in zip(pattern, ["A", "B", "C", "D", "E"], scores):
            if pi == 0:
                continue

            user += name
            summed_score += score

        if len(user) == 0:
            continue

        ans.append((summed_score, user))

    ans = sorted(ans, key=lambda x: (-x[0], x[1]))

    for _, name in ans:
        print(name)


if __name__ == "__main__":
    main()
