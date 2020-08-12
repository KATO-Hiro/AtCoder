# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    n, m = map(int, input().split())
    sta = [defaultdict(int) for _ in range(n)]
    ans = 0

    # See:
    # https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2018/1117_code_festival_2018_final
    for line in sys.stdin.readlines():
        ai, bi, li = map(int, line.split())
        ai -= 1
        bi -= 1

        # Count links
        ri = 2540 - li
        ans += sta[ai][ri]
        ans += sta[bi][ri]

        # Update link count
        sta[ai][li] += 1
        sta[bi][li] += 1

    print(ans)


if __name__ == '__main__':
    main()
