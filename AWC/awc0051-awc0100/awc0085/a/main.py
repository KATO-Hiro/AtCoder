# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    t = [(i, si) for i, si in enumerate(s)]
    round = 1
    ans = [0] * n

    while len(t) >= 2:
        winners = []
        size = len(t)

        for i in range(0, size, 2):
            j, tj = t[i]
            k, tk = t[i + 1]

            if tj > tk:
                ans[k] = round
                winners.append((j, tj))
            elif tj < tk:
                ans[j] = round
                winners.append((k, tk))

        t = winners
        round += 1

    print(*ans)


if __name__ == "__main__":
    main()
