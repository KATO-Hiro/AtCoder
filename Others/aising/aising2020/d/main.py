# -*- coding: utf-8 -*-


def calc_remainder(number: str, base: int = 2, mod: int = 10 ** 9 + 7):
    remainder = 0

    for digit_value in number:
        remainder *= base
        remainder %= mod

        remainder += int(digit_value)

    return remainder


def calc_popcount(number: int) -> int:
    # See:
    # https://nixeneko.hatenablog.com/entry/2018/03/04/000000
    return bin(number).count("1")


def count_operation(number: int) -> int:
    if number == 0:
        return 1
    else:
        return count_operation(number % calc_popcount(number)) + 1


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = input().rstrip()

    popcount = x.count("1")
    ans = [0 for _ in range(n)]

    for bit in [0, 1]:
        if bit == 0:
            current_popcount = popcount + 1
        else:
            current_popcount = popcount - 1

        # ゼロ除算を回避
        if current_popcount <= 0:
            continue

        # q0 = x % current_popcountを求める
        q0 = calc_remainder(number=x, base=2, mod=current_popcount)

        # 0から1、もしくは、1から0にしたときの差分について
        # q = x[j] % current_popcountを求める
        digit_count = 1

        for j in range(n - 1, -1, -1):
            if int(x[j]) == bit:
                q = q0

                if bit == 0:
                    q = (q + digit_count) % current_popcount
                else:
                    # 負の値を回避
                    q = (q - digit_count + current_popcount) % current_popcount

                ans[j] = count_operation(q)

            digit_count *= 2
            digit_count %= current_popcount

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
