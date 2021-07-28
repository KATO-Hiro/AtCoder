# -*- coding: utf-8 -*-


def f(a, k, l, candidate):
    count = 0
    prev = 0

    for ai in a:
        if ai - prev >= candidate and l - ai >=candidate:
            count += 1
            prev = ai
    
    if count >= k:
        return True
    else:
        return False


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split())) + [l]
    left = -1
    right = l + 1

    while (right - left) > 1:
        candidate = (left + right) // 2
        ok = f(a, k, l, candidate)

        if ok:
            left = candidate
        else:
            right = candidate

    print(left)


if __name__ == "__main__":
    main()
