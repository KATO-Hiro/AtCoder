# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys

    input = sys.stdin.readline

    h, a, b, c, d = map(int, input().split())
    ans = float("inf")

    def f(op2_count):
        remain, cost = h, 0

        for i in range(op2_count):
            remain -= c
            cost += d

            if remain > 0:
                remain -= remain // 2

        return remain, cost

    for op2_count in range(40):
        remain, cost = f(op2_count)

        if remain > 0:
            cost += ceil(remain, a) * b

        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
