# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left

    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    time_a = a[0] + x
    time_b = b[0] + y  # dummy
    try_count = 0
    ai = 0
    bi = 0
    use_a = [0 for _ in range(n)]
    use_b = [0 for _ in range(m)]
    use_a[0] = 1

    # 出発時間と到着時間をそれぞれ計算して，二分探索
    while ai < n and bi < m:
        if try_count % 2 == 0:
            bi = bisect_left(b, time_a)

            if bi == m:
                break

            use_b[bi] = 1
            time_b = b[bi] + y
        else:
            ai = bisect_left(a, time_b)

            if ai == n:
                break

            use_a[ai] = 1
            time_a = a[ai] + x

        try_count += 1

    print(min(sum(use_a), sum(use_b)))


if __name__ == '__main__':
    main()
