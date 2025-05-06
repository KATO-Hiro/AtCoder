# -*- coding: utf-8 -*-

inf = 10**20


def find_max_with_digit_sum(x, y):
    """
    整数x以下で各桁の和がyとなる最大の整数を返す
    存在しない場合は-1を返す
    """
    x_str = str(x)
    n = len(x_str)

    # (桁位置, 桁和, x未満確定フラグ) -> 最大値
    memo = {}

    def dp(pos, digit_sum, is_less):
        """
        pos: 現在見ている桁位置
        digit_sum: 残りの必要な桁和
        is_less: 現在までの桁でx未満が確定しているかどうか
        """
        if pos == n:
            return 0 if digit_sum == 0 else -inf

        if (pos, digit_sum, is_less) in memo:
            return memo[(pos, digit_sum, is_less)]

        value_max = -inf

        limit = 9 if is_less else int(x_str[pos])

        for d in range(limit, -1, -1):
            if digit_sum - d < 0:
                continue

            next_is_less = is_less or (d < int(x_str[pos]))
            next_val = dp(pos + 1, digit_sum - d, next_is_less)

            if next_val != -inf:
                curr_val = d * (10 ** (n - pos - 1)) + next_val
                value_max = max(value_max, curr_val)
                break

        memo[(pos, digit_sum, is_less)] = value_max
        return value_max

    result = dp(0, y, False)
    return result if result != -inf else -1


def main():
    import sys

    input = sys.stdin.readline

    a, b, x = map(int, input().split())
    ans = 1
    ans_max = 10**9

    # d(n)の取りうる範囲は、[1, 9 * 9 + 1)のはず
    for dn in range(1, 82):
        x2 = x - b * dn

        if x2 <= 0:
            continue

        n = find_max_with_digit_sum(x2 // a, dn)
        ans = max(ans, n)
        ans = min(ans, ans_max)

    print(ans)


if __name__ == "__main__":
    main()
