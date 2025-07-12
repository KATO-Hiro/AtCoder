# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    def f(a, b):
        result = []
        id = 0

        for i, ai in enumerate(a):
            if b[id] != ai:
                continue

            result.append(i)
            id += 1

            if len(result) == len(b):
                return result

        return [-1]

    ans1 = f(a, b)
    ans2 = f(a[::-1], b[::-1])
    ans2 = [n - 1 - i for i in ans2[::-1]]

    if ans1 == [-1] or ans2 == [-1] or ans1 == ans2:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
