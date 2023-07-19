# -*- coding: utf-8 -*-

ans = set()


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    k = int(input())
    number = list()

    def dfs(digit, upper):
        if digit == upper:
            n = int("".join(map(str, number)))
            ans.add(n)
            return

        for i in range(10):
            if len(number) >= 1 and abs(number[-1] - i) > 1:
                continue

            number.append(i)
            dfs(digit + 1, upper)
            number.pop()

    for i in range(1, 11):
        dfs(0, i)

    # print(sorted(ans))
    print(sorted(ans)[k])


if __name__ == "__main__":
    main()
