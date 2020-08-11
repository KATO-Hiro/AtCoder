# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = list()

    for i in range(n):
        k = i
        count = 1

        while True:
            if (a[k] - 1) == i:
                ans.append(count)
                break
            else:
                count += 1
                k = a[k] - 1

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
