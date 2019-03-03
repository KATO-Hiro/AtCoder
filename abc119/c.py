# -*- coding: utf-8 -*-


def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]

    # See:
    # https://img.atcoder.jp/abc119/editorial.pdf
    # http://drken1215.hatenablog.com/entry/2019/02/24/224100?_ga=2.107425799.427838713.1551485650-1201012407.1527836447#fnref:1
    # https://atcoder.jp/contests/abc119/submissions/4372229
    def dfs(i, cur_a, cur_b, cur_c):
        if i == n:
            if cur_a == 0 or cur_b == 0 or cur_c == 0:
                return float('inf')
            return abs(a - cur_a) + abs(b - cur_b) + abs(c - cur_c)

        w = dfs(i + 1, cur_a, cur_b, cur_c)
        x = dfs(i + 1, cur_a + l[i], cur_b, cur_c) + 10 * (cur_a != 0)
        y = dfs(i + 1, cur_a, cur_b + l[i], cur_c) + 10 * (cur_b != 0)
        z = dfs(i + 1, cur_a, cur_b, cur_c + l[i]) + 10 * (cur_c != 0)

        return min(w, x, y, z)

    print(dfs(0, 0, 0, 0))


if __name__ == '__main__':
    main()
