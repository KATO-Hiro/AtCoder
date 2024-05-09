# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    x = list(map(int, input().split()))
    cost_a, cost_b, cost_c = 0, b, c

    for xi in x:
        cost_a += max(0, xi - 3) * a
        cost_b += max(0, xi - 50) * a

    print(min(cost_a, cost_b, cost_c))


if __name__ == "__main__":
    main()
