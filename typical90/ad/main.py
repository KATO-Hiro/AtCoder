# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    count = [0] * (n + 1)

    for i in range(2, n + 1):
        if count[i] != 0:
            continue

        for j in range(i, n + 1, i):
            count[j] += 1
    
    ans = sum([1 for c in count if c >= k])
    print(ans)


if __name__ == "__main__":
    main()
