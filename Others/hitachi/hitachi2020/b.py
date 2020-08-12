# -*- coding: utf-8 -*-


def main():
    a, b, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_a = min(a)
    min_b = min(b)
    ans = min_a + min_b

    for i in range(m):
        xi, yi, ci = map(int, input().split())
        xi -= 1
        yi -= 1

        ans = min(ans, a[xi] + b[yi] - ci)

    print(ans)


if __name__ == '__main__':
    main()
