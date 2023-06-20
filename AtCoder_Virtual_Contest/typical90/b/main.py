# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    ans = list()

    for pattern in product(["(", ")"], repeat=n):
        flag = True
        count = 0

        for pi in pattern:
            if pi == "(":
                count += 1
            else:
                count -= 1

                if count < 0:
                    flag = False
                    break

        if count == 0 and flag:
            ans.append(pattern)

    for ans_i in sorted(ans):
        print("".join(ans_i))


if __name__ == "__main__":
    main()
