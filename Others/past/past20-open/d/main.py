# -*- coding: utf-8 -*-


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: list[list]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = [list(input().rstrip()) for _ in range(n)]
    a = rotate_90_degrees_to_right(c)

    for ai in a:
        ans = list()

        for aij in ai:
            if aij == "v":
                ans.append("<")
            elif aij == "^":
                ans.append(">")
            elif aij == "<":
                ans.append("^")
            else:
                ans.append("v")

        print("".join(ans))


if __name__ == "__main__":
    main()
