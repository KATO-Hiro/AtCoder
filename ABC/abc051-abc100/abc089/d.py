# -*- coding: utf-8 -*-


def main():
    h, w, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    pieces = [0] * (h * w + 1)
    cost = [0 for _ in range(h * w + 1)]

    for hi in range(h):
        for wi in range(w):
            number = a[hi][wi]
            pieces[number] = (hi, wi)

    # See:
    # https://img.atcoder.jp/abc089/editorial.pdf
    # https://www.youtube.com/watch?v=EDq1rl-6YcQ
    for i in range(d + 1, h * w + 1):
        prev_piece = pieces[i - d]
        next_piece = pieces[i]

        cost[i] = cost[i - d] + \
            abs(next_piece[1] - prev_piece[1]) + \
            abs(next_piece[0] - prev_piece[0])

    q = int(input())
    ans = [0 for _ in range(q)]

    for j in range(q):
        lj, rj = map(int, input().split())
        ans[j] = cost[rj] - cost[lj]

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
