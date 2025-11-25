# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    digit_max = 11
    aj = [[] for _ in range(digit_max)]

    # ai * 10 ** digit + aj ≡ 0 (mod m)
    # 桁ごとに分解
    for ai in a:
        d = len(str(ai))
        aj[d].append(ai % m)

    ten = 1
    ans = 0

    for digit in range(digit_max):
        freq = defaultdict(int)

        for mod_ai in aj[digit]:
            freq[mod_ai] += 1

        for ai in a:
            ak = (-ai * ten) % m
            ans += freq[ak]

        ten *= 10
        ten %= m

    print(ans)


if __name__ == "__main__":
    main()
