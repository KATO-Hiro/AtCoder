# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    # sをsortしてから、あるsiに対して辞書順で前後の2つを比較
    t = sorted([(si, i) for i, si in enumerate(s)])
    ans = [0] * n

    for (x, i), (y, j) in zip(t, t[1:]):
        count = 0

        for xk, yk in zip(x, y):
            if xk != yk:
                break

            count += 1
        
        ans[i] = max(ans[i], count)
        ans[j] = max(ans[j], count)

    for i in range(n):
        print(ans[i])


if __name__ == "__main__":
    main()
