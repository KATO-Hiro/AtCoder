# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = deque()
    cur_sum, cur_xor = 0, 0
    ans = 0

    # 尺取り法(deque Ver)
    for ai in a:
        d.append(ai)
        cur_sum += ai
        cur_xor ^= ai

        while d and not (cur_sum == cur_xor):
            di = d.popleft()
            cur_sum -= di
            cur_xor ^= di
        
        ans += len(d)

    print(ans)


if __name__ == "__main__":
    main()
