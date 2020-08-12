# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(input())
    black_count = [0 for _ in range(n + 1)]
    ans = float('inf')

    for i, si in enumerate(s):
        if si == '#':
            black_count[i + 1] = black_count[i] + 1
        else:
            black_count[i + 1] = black_count[i]

    for j in range(n + 1):
        ans = min(ans, black_count[j] + (n - j) - black_count[n] + black_count[j])

    print(ans)


if __name__ == '__main__':
    main()
