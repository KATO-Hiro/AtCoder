# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split()))) + [float("inf")]
    visited = [False for _ in range(n + 1)]
    ans = 0

    for index, ai in enumerate(a[:-1]):
        if visited[index]:
            continue

        visited[index] = True
        bi = ai

        for i in range(40):
            bi *= 2
            pos = bisect_left(a, bi)

            if a[pos] == bi:
                visited[pos] = True

            if pos == n:
                break

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
