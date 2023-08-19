# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    sys.setrecursionlimit(10**8)

    n = int(input())
    digit = len(list(str(n)))

    def dfs(i, a, d):
        if i == d:
            if a.count(3) == 0 or a.count(5) == 0 or a.count(7) == 0:
                return 0

            value = int("".join(map(str, a)))

            if 1 <= value <= n:
                # print(a)
                return 1
            else:
                return 0

        results = 0

        for j in [3, 5, 7]:
            a.append(j)
            results += dfs(i + 1, a, d)
            a.pop()

        return results

    ans = 0

    for d in range(1, digit + 1):
        ans += dfs(0, [], d)

    print(ans)


if __name__ == "__main__":
    main()
