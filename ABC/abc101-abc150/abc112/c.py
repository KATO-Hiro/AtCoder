# -*- coding: utf-8 -*-


def main():
    n = int(input())
    xs = list()
    ys = list()
    hs = list()

    # See:
    # https://beta.atcoder.jp/contests/abc112/submissions/3360331
    # https://img.atcoder.jp/abc112/editorial.pdf
    # https://www.youtube.com/watch?v=CURWJ1Dr44A
    for i in range(n):
        xi, yi, hi = map(int, input().split())
        xs.append(xi)
        ys.append(yi)
        hs.append(hi)

        # Record a position satisfying the task conditions.
        if hi > 0:
            pos = i

    for cx in range(100 + 1):
        for cy in range(100 + 1):
            is_consistent = True
            candidate_height = abs(xs[pos] - cx) + abs(ys[pos] - cy) + hs[pos]

            for i in range(n):
                each_height = max(candidate_height - abs(xs[i] - cx) - abs(ys[i] - cy), 0)

                if hs[i] != each_height:
                    is_consistent = False
                    break

            if is_consistent:
                print(cx, cy, candidate_height)
                exit()


if __name__ == '__main__':
    main()
