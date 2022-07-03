# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ans = float("inf")
    time_sum = 0
    
    for i in range(n):
        ai, bi = ab[i]
        time_sum += ai + bi
        x -= 1

        if x >= 0:
            ans = min(ans, time_sum + bi * x)

    print(ans)


if __name__ == "__main__":
    main()
