# -*- coding: utf-8 -*-


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: list[list]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    t = rotate_90_degrees_to_right(s)
    ans = 0

    for ti in t:
        if ti.count(".") == h:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
