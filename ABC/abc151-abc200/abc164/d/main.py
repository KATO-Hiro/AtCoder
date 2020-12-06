# -*- coding: utf-8 -*-


def main():
    s = input()

    mod = 2019
    freq = [0 for _ in range(mod)]

    digit = 1
    summed = 0
    ans = 0

    for si in reversed(s):
        freq[summed] += 1

        summed += int(si) * digit
        summed %= mod

        ans += freq[summed]

        digit *= 10
        digit %= mod

    print(ans)


if __name__ == "__main__":
    main()
