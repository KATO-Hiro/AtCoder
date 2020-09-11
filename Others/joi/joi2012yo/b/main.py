# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    win_count = [0 for _ in range(n)]
    draw_count = [0 for _ in range(n)]

    for i in range(n * (n - 1) // 2):
        ai, bi, ci, di = map(int, input().split())

        if ci > di:
            win_count[ai - 1] += 1
        elif ci < di:
            win_count[bi - 1] += 1
        else:
            draw_count[ai - 1] += 1
            draw_count[bi - 1] += 1

    points = [0 for _ in range(n)]

    for j in range(n):
        points[j] = (j + 1, win_count[j] * 3 + draw_count[j])

    p = sorted(points, key=lambda x: x[1], reverse=True)
    prev = p[0][0] - 1

    ans = [0 for _ in range(n)]
    ans[prev] = 1

    count = 2

    for first, second in zip(p, p[1:]):
        if first[1] == second[1]:
            ans[second[0] - 1] = ans[first[0] - 1]
        else:
            ans[second[0] - 1] = count

        count += 1

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
