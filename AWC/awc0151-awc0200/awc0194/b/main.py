# -*- coding: utf-8 -*-


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: list[list]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    t = rotate_90_degrees_to_right(s)
    ans = -1
    candidate = -1

    for i, ti in enumerate(t, 1):
        count = ti.count("F")

        if count > candidate:
            ans = i
            candidate = count

    print(ans)


if __name__ == "__main__":
    main()
