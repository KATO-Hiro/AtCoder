# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l1, r1, l2, r2  = map(int, input().split())
    arr = [0] * 101

    for i in range(l1, r1 + 1):
        arr[i] += 1

    for i in range(l2, r2 + 1):
        arr[i] += 1
    
    ans = 0

    for ai in arr:
        if ai == 2:
            ans += 1
    
    if ans > 0:
        ans -= 1

    print(ans)


if __name__ == "__main__":
    main()
