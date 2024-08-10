# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    size = 10**6 + 1
    numbers = [0] * size
    ans = 0

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x = qi[1]
            numbers[x] += 1

            if numbers[x] == 1:
                ans += 1
        elif qi[0] == 2:
            x = qi[1]
            numbers[x] -= 1

            if numbers[x] == 0:
                ans -= 1
        else:
            print(ans)


if __name__ == "__main__":
    main()
