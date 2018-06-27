'''input
3 2
..#
.#.
#.#
#.
.#
Yes

3 2
#.#
.#.
#.#
#.
.#
Yes

4 1
....
....
....
....
#
No

3 2
.#.
.#.
#.#
#.
.#
Yes

3 2
..#
#..
.#.
#.
.#
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    a = [list(input()) for _ in range(n)]
    b = [list(input()) for _ in range(m)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            is_exist = True

            # See:
            # https://beta.atcoder.jp/contests/abc054/submissions/1103264
            for dx in range(m):
                if a[i + dx][j:j + m] != b[dx]:
                    is_exist = False
                    break

            if is_exist:
                print('Yes')
                exit()

    print('No')
