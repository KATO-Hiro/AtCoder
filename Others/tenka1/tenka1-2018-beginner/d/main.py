# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    k = 0

    # 条件を満たすかどうかを判定
    while k * (k - 1) < 2 * n:
        k += 1
    
    if k * (k - 1) != 2 * n:
        print("No")
        exit()
    else:
        print("Yes")
        print(k)
    
    # 部分集合を列挙
    value = 1
    ans = [[] for _ in range(k)]

    for i in range(k):
        for j in range(i + 1, k):
            ans[i].append(value)
            ans[j].append(value)

            value += 1
    
    for a in ans:
        print(len(a), *a)


if __name__ == "__main__":
    main()
