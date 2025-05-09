# -*- coding: utf-8 -*-


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: list[list]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [list(input().rstrip()) for _ in range(n)]
    t = [list(input().rstrip()) for _ in range(n)]
    inf = 10**9
    ans = inf

    for i in range(4):
        count = i

        for j in range(n):
            for k in range(n):
                if s[j][k] != t[j][k]:
                    count += 1

        ans = min(ans, count)
        s = rotate_90_degrees_to_right(s)

    print(ans)


if __name__ == "__main__":
    main()
