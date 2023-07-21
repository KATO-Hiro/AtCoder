# -*- coding: utf-8 -*-


from collections import Counter


def is_win_takahashi(s, t):
    ct, ca = Counter(s), Counter(t)
    summed_t, summed_a = 0, 0

    for i in range(1, 10):
        summed_t += i * (10 ** ct[str(i)])
        summed_a += i * (10 ** ca[str(i)])

    if summed_t > summed_a:
        return True
    else:
        return False


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    s = input().rstrip()[:-1]
    t = input().rstrip()[:-1]
    remain = [k] * 10
    remain[0] = 0

    for si, ti in zip(s, t):
        remain[int(si)] -= 1
        remain[int(ti)] -= 1

    win_count = 0

    # 残り1枚を1〜9の範囲で決める。所有枚数未満なら、選ばない。
    for i in range(1, 10):
        tmp_s = s + str(i)

        for j in range(1, 10):
            tmp_t = t + str(j)

            if not is_win_takahashi(list(tmp_s), list(tmp_t)):
                continue

            if i == j:
                win_count += remain[i] * (remain[i] - 1)
            else:
                win_count += remain[i] * remain[j]

    # 残りの枚数を区別して選ぶ
    count = 9 * k - 8  # 表向きのカードを除外
    total_pattern = count * (count - 1)
    # print(win_count)
    # print(total_pattern)
    print(win_count / total_pattern)


if __name__ == "__main__":
    main()
