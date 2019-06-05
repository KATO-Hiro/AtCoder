# -*- coding: utf-8 -*-


def main():
    d, g = map(int, input().split())
    ps = [0 for _ in range(d)]
    cs = [0 for _ in range(d)]
    score_with_bonus = dict()
    ans = float('inf')

    for i in range(d):
        pi, ci = map(int, input().split())
        ps[i] = pi
        cs[i] = ci
        score_with_bonus[i] = (i + 1) * pi * 100 + ci

    # See:
    # https://img.atcoder.jp/abc104/editorial.pdf
    for bit in range(1 << d):
        total_score = 0
        problem_count = 0
        pmax = 0

        for j in range(d):
            if bit & (1 << j):
                total_score += score_with_bonus[j]
                problem_count += ps[j]
            else:
                pmax = max(pmax, j)

        for k in range(1, ps[pmax]):
            if total_score < g:
                total_score += (pmax + 1) * 100
                problem_count += 1

        if problem_count > 0 and total_score >= g:
            ans = min(ans, problem_count)

    print(ans)


if __name__ == '__main__':
    main()
