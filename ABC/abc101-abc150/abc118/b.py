# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    ans = [0 for _ in range(30)]

    for i in range(n):
        ka = list(map(int, input().split()))

        for j in ka[1:]:
            ans[j - 1] += 1

    result = 0

    for a in ans:
        if a == n:
            result += 1

    print(result)


if __name__ == '__main__':
    main()
