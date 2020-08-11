# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    reverse_v = v[::-1]
    ans = 0

    # See:
    # https://www.youtube.com/watch?v=m-Nov1EvGoc
    for left in range(k + 1):
        for right in range(k - left + 1):
            if left + right > n:
                continue

            remain = k - (left + right)
            merged_v = sorted(v[:left] + reverse_v[:right])
            merged_v_len = len(merged_v)
            minus = 0

            for i in range(min(remain, merged_v_len)):
                if merged_v[i] < 0:
                    minus += merged_v[i]

            ans = max(ans, sum(merged_v) - minus)

    print(ans)


if __name__ == '__main__':
    main()
