# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for j in range(1, n - 1):
        left = a[:j]
        right = a[j + 1:]

        left_count = 0
        right_count = 0

        for li in left:
            if li < a[j]:
                left_count += 1

        for ri in right:
            if a[j] > ri:
                right_count += 1

        ans += left_count * right_count

    print(ans)


if __name__ == '__main__':
    main()
