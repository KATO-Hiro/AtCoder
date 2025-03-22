# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    s = list(input().rstrip())
    n = len(s)

    for digit in range(n):
        start = 0

        if digit == 0:
            start = 1

        for number in range(start, 10):
            ok = True

            t = s.copy()
            t[digit] = str(number)

            for first, second in pairwise(t):
                diff = abs(int(second) - int(first))

                if diff >= 2:
                    ok = False
                    break

            if ok:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
