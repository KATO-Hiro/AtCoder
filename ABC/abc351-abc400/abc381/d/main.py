# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for start in range(2):
        right = start
        c = Counter()

        for left in range(start, n, 2):
            while right + 1 < n:
                if a[right] != a[right + 1]:
                    break
                if c[a[right]] == 1:
                    break

                c[a[right]] += 1
                right += 2

            ans = max(ans, right - left)

            if right == left:
                right += 2
            else:
                c[a[left]] -= 1

    print(ans)


if __name__ == "__main__":
    main()
