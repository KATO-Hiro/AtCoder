# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    right = 0
    cur_sum, cur_xor = 0, 0
    size = 0
    ans = 0

    # 尺取り法
    for left in range(n):
        while right < n and (cur_sum + a[right] == cur_xor ^ a[right]):
            cur_sum += a[right]
            cur_xor ^= a[right]
            right += 1
            size += 1

        ans += size

        # 後処理
        size -= 1
        cur_sum -= a[left]
        cur_xor ^= a[left]

    print(ans)



if __name__ == "__main__":
    main()
