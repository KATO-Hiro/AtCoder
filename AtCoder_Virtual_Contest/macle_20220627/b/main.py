# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ans = 0.0

    for i in range(1, n + 1):
        j = i
        count = 0

        while j < k:
            j *= 2
            count += 1
        
        ans += (1 / 2) ** count

    print(ans / n)


if __name__ == "__main__":
    main()
