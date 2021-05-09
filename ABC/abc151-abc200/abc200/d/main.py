# -*- coding: utf-8 -*-


def output(number: int):
    ans = list()
    i = 1

    while number:
        if number & 1:
            ans.append(i)

        i += 1
        number >>= 1

    print(len(ans), *ans)


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n = min(n, 8)
    a = list(map(int, input().split()))
    candidates = [0 for _ in range(200)]

    for bit in range(1, 1 << n):
        summed = 0

        for j in range(n):
            if bit >> j & 1:
                summed += a[j]
                summed %= 200

        if candidates[summed] == 0:
            candidates[summed] = bit
        else:
            print("Yes")
            output(bit)
            output(candidates[summed])
            exit()

    print("No")


if __name__ == "__main__":
    main()
