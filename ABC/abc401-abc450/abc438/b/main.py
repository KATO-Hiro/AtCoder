# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()
    inf = 10**18
    ans = inf

    for i in range(n):
        if i + m > n:
            break

        count = 0

        for j in range(m):
            diff = int(s[i + j]) - int(t[j])

            if diff < 0:
                diff += 10

            count += diff

        ans = min(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
