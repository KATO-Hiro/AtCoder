# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = 1
    ans = list()

    while n:
        if n % 3 == 1:
            ans.append(x)
            n -= 1
        elif n % 3 == 2:
            ans.append(-x)
            n += 1

        n //= 3
        x *= 3

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
