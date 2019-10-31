# -*- coding: utf-8 -*-


def main():
    n, d, k = map(int, input().split())
    ans = [0 for _ in range(k)]
    cur = [0 for _ in range(k)]
    goal = [0 for _ in range(k)]
    direct = [0 for _ in range(k)]
    reached = [False for _ in range(k)]
    lr = list()

    for i in range(d):
        li, ri = map(int, input().split())
        lr.append((li, ri))

    # 始点，終点，向きをメモ
    for i in range(k):
        si, ti = map(int, input().split())
        cur[i] = si
        goal[i] = ti

        # 始点のほうが終点よりも右側にある場合
        if si > ti:
            direct[i] = 1

    # 各日でそれぞれの民族が移動できる右端もしくは左端を計算
    # 計算量はO(DK)
    for day, (li, ri) in enumerate(lr, 1):
        for i in range(k):
            if direct[i] == 0:
                if not reached[i] and (li <= cur[i] <= ri):
                    cur[i] = max(cur[i], ri)
                    ans[i] = day

                    if cur[i] >= goal[i]:
                        reached[i] = True
            else:
                if not reached[i] and (li <= cur[i] <= ri):
                    cur[i] = min(cur[i], li)
                    ans[i] = day

                    if cur[i] <= goal[i]:
                        reached[i] = True

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
