# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    results = []

    for i in range(h):
        si = input().rstrip()
        summed = 0

        for sij in si:
            summed += int(sij)

        results.append((summed, i + 1))

    results = sorted(results, key=lambda x: (x[0], x[1]))
    ans = results[0][1]
    print(ans)


if __name__ == "__main__":
    main()
