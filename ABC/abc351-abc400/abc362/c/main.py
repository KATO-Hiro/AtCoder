# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    left, right = list(), list()

    for i in range(n):
        li, ri = map(int, input().split())
        left.append(li)
        right.append(ri)

    summed_left = sum(left)
    summed_right = sum(right)

    if summed_left <= 0 <= summed_right:
        print("Yes")
    else:
        print("No")
        exit()

    ans = left
    remain = -summed_left

    for i, (li, ri) in enumerate(zip(left, right)):
        diff = ri - li

        if diff < remain:
            ans[i] = ri
            remain -= diff
        else:
            ans[i] = li + remain
            break

    print(*ans)


if __name__ == "__main__":
    main()
