# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    # a % k == b % k == c % k
    # (a + b) % k == 0が成り立つには、mod k == 0 or k / 2である必要がある
    count1, count2 = 0, 0

    for i in range(1, n + 1):
        if i % k == 0:
            count1 += 1

    if k % 2 == 0:
        for i in range(1, n + 1):
            if i % k == k // 2:
                count2 += 1
    
    ans = count1 ** 3 + count2 ** 3
    print(ans)


if __name__ == "__main__":
    main()
