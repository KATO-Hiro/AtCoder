# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    k = int(input())

    # '.'の数を前計算しておく
    dot_count = [0] * (n + 1)

    for i, si in enumerate(s):
        dot_count[i + 1] = dot_count[i]

        if si == ".":
            dot_count[i + 1] += 1

    right = 0
    ans = 0

    # 尺取り法
    for left in range(n):
        while (right < n) and (dot_count[right + 1] - dot_count[left]) <= k:
            right += 1

        ans = max(ans, right - left)

    print(ans)


if __name__ == "__main__":
    main()
