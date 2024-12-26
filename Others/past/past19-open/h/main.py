# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations, product

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    for pattern in permutations(a):
        t = []

        for pi in pattern:
            t.append(pi)
            t.append("")

        for op in product(["+", "*"], repeat=n - 1):
            for i, op_i in enumerate(op):
                t[2 * i + 1] = op_i

            u = t[:]
            u = "".join(map(str, u))

            if eval(u) == s:
                print("Yes")
                print(u.replace("*", "x"))
                exit()

    print("No")


if __name__ == "__main__":
    main()
