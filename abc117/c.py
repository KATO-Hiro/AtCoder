# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    xs = sorted(list(map(int, input().split())))

    if n >= m:
        print(0)
    else:
        ans = xs[-1] - xs[0]
        diff = [0 for _ in range(m - 1)]

        for i in range(m - 1):
            diff[i] = xs[i + 1] - xs[i]

        print(ans - sum(sorted(diff, reverse=True)[:n - 1]))


if __name__ == '__main__':
    main()
