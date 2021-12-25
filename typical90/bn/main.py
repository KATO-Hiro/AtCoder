# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0.0

    for i in range(n):
        for j in range(i + 1, n):
            total = (lr[i][1] - lr[i][0] + 1) * (lr[j][1] - lr[j][0] + 1)
            met = 0

            for k in range(lr[i][0], lr[i][1] + 1):
                met += max(0, min(k, lr[j][1] + 1) - lr[j][0])

            ans += met / total

    print(ans)


if __name__ == "__main__":
    main()
