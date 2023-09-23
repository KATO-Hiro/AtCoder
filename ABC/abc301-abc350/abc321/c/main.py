# -*- coding: utf-8 -*-

numbers = set()


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    k = int(input())

    def dfs(i, a):
        if len(a) >= 1 and a[-1] <= y:
            m = "".join(map(str, a))
            numbers.add(int(m))
            return

        for j in range(i - 1, -1, -1):
            a.append(j)
            dfs(j, a)
            a.pop()

    for x in range(1, 10 + 1):
        for y in range(x + 1):
            dfs(x, [])

    print(sorted(numbers)[k])


if __name__ == "__main__":
    main()
