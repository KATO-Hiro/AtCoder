# -*- coding: utf-8 -*-


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: list[list]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    ans = ""

    for i, si in enumerate(s, 1):
        if si.count("x") == m:
            ans = "Faucet " + str(i)
            break

    t = rotate_90_degrees_to_right(s)

    for j, tj in enumerate(t, 1):
        if tj.count("x") == n:
            ans = "Drain " + str(j)
            break

    print(ans)


if __name__ == "__main__":
    main()
