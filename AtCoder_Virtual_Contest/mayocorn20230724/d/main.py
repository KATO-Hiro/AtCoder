# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, n, hi, wj = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    count_all = defaultdict(int)

    for i in range(h):
        for j in range(w):
            count_all[a[i][j]] += 1

    # print(count_all)
    ans = list()

    for k in range(h - hi + 1):
        count_partly = defaultdict(int)
        candidates = list()

        for i in range(k, k + hi):
            for j in range(wj):
                count_partly[a[i][j]] += 1

        count = 0

        for key, value in count_all.items():
            if value - count_partly[key] > 0:
                count += 1

        candidates.append(count)

        for x in range(wj, w):
            count = 0

            for y in range(k, k + hi):
                count_partly[a[y][x]] += 1
                count_partly[a[y][x - wj]] -= 1

            for key, value in count_all.items():
                if value - count_partly[key] > 0:
                    count += 1

            candidates.append(count)

        ans.append(candidates)

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
