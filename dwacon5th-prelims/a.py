# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    diff = float('inf')
    ans = 0
    ave = sum(a) / n

    for i, ai in enumerate(a):
        if abs(ai - ave) < diff:
            diff = abs(ai - ave)
            ans = i

    print(ans)


if __name__ == '__main__':
    main()
