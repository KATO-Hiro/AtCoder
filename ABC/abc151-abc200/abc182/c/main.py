# -*- coding: utf-8 -*-


def main():
    from itertools import product

    s = list(input())
    n = len(s)

    comb = list(product([0, 1], repeat=n))
    ans = float("inf")

    for c in comb:
        number = ""
        zero_count = 0

        for index, ci in enumerate(c):
            if ci == 1:
                number += s[index]
            else:
                zero_count += 1

        if number == "":
            continue

        if int(number) % 3 == 0:
            ans = min(ans, zero_count)

    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
