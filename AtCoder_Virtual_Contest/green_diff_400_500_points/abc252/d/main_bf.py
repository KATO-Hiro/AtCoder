# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    # ans = 0
    ans = list()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] == a[j]:
                    continue
                if a[j] == a[k]:
                    continue
                if a[k] == a[i]:
                    continue

                ans.append((a[i], a[j], a[k]))

    print(len(ans))


if __name__ == "__main__":
    main()
