# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    array = []
    a = [str(2**i) for i in range(30)]
    candidates = set()

    def dfs(i):
        number = "".join(map(str, array))

        if array and len(number) > i:
            return

        if array and len(number) == i:
            if number not in candidates and int(number) <= 10**9:
                candidates.add(int(number))

            return

        for ai in a:
            array.append(ai)
            dfs(i)
            array.pop()

    for i in range(1, 10):
        dfs(i)

    candidates = sorted(candidates)
    print(candidates[n - 1])


if __name__ == "__main__":
    main()
