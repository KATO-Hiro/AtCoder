# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    ans = 1

    for w in range(1, n + 1):
        best = 1

        for start in range(w):
            candidate = 1
            prev = h[start]

            for step in range(start + w, n, w):
                if step >= n:
                    break

                if h[step] == prev:
                    candidate += 1
                else:
                    best = max(best, candidate)
                    candidate = 1

                prev = h[step]

            best = max(best, candidate)

        ans = max(ans, best)

    print(ans)


if __name__ == "__main__":
    main()
