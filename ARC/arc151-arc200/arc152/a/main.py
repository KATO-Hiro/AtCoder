# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    # 1つ席を空けながら前の組から座る
    # 最後の2人組に到達したときに残りの席が2以上ならYes
    k = n

    for j in range(n - 1, -1, -1):
        if a[j] == 2:
            k = j
            break

    if k == n:
        if a[-1] == 2:
            print("No")
        elif a[-1] == 1:
            print("Yes")

        exit()

    summed = 0

    for i in range(k):
        summed += a[i] + 1

    if l - summed >= 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
