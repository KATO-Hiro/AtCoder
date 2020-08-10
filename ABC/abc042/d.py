# -*- coding: utf-8 -*-

# See:
# http://drken1215.hatenablog.com/entry/2018/06/08/210000
max_value = 500050
mod = 10 ** 9 + 7

fac = [0 for _ in range(max_value)]
finv = [0 for _ in range(max_value)]
inv = [0 for _ in range(max_value)]


def com_init():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, max_value):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def com(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def main():
    h, w, a, b = map(int, input().split())
    x = h - (a + 1)
    com_init()
    prev = 0
    ans = 0
    com_xy = [0 for _ in range(w - b)]
    com_za = [0 for _ in range(w - b)]
    i = 0
    j = 0

    for y in range(b, w):
        com_xy[i] = com(x + y, y)
        i += 1

    for z in range((w - (b + 1) + a), a - 1, -1):
        com_za[j] = com(z, z - a)
        j += 1

    for xy, za in zip(com_xy, com_za):
        ans += (xy - prev) * za
        ans %= mod
        prev = xy

    print(ans)


if __name__ == '__main__':
    main()
