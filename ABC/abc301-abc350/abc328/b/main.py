# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = list(map(int, input().split()))
    ans = 0

    for i, di in enumerate(d, 1):
        for j in range(1, di + 1):
            result = set(str(i) + str(j))

            if len(result) == 1:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
