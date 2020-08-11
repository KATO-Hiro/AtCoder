# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m, q = map(int, input().split())
    points = [n for _ in range(m)]
    solved = [[False for _ in range(m)] for _ in range(n)]

    for i in range(q):
        si = list(map(int, input().split()))
        ni = si[1] - 1

        if si[0] == 1:
            score = 0

            for p, s in zip(points, solved[ni]):
                if s:
                    score += p

            print(score)
        else:
            mi = si[2] - 1
            solved[ni][mi] = True
            points[mi] -= 1


if __name__ == '__main__':
    main()
