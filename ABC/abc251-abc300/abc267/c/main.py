# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    summed, total = 0, 0

    # 最初だけ愚直に
    for i in range(1, m + 1):
        summed += i * a[i - 1]
        total += a[i - 1]

    ans = summed
    
    # 差分を計算
    for i in range(m, n):
        n_summed = summed - total + a[i] * m 
        n_total = total - a[i - m]+ a[i] 
        ans = max(ans, n_summed)

        summed = n_summed
        total = n_total

    print(ans)


if __name__ == "__main__":
    main()
