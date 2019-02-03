# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_right
    from bisect import bisect_left

    n = int(input())
    t = list(map(int, input().split()))
    a = list(map(int, input().split()))[::-1]
    t_candidates = [1 for _ in range(n)]
    a_candidates = [1 for _ in range(n)]
    ans = 1

    if max(t) != max(a):
        print(0)
        exit()
    else:
        if bisect_left(t, max(t)) > (n - bisect_left(a, max(a)) - 1):
            print(0)
            exit()

    for i in range(1, n):
        if t[i] == t[i - 1]:
            t_candidates[i] = t[i]

        if a[i] == a[i - 1]:
            a_candidates[i] = a[i]

    for t_candidate, a_candidate in zip(t_candidates, a_candidates[::-1]):
        ans *= min(t_candidate, a_candidate)
        ans %= 10 ** 9 + 7

    print(ans)


if __name__ == '__main__':
    main()
