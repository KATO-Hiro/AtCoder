# -*- coding: utf-8 -*-


def popcount(n: int) -> int:
    return bin(n).count("1")


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    q = int(input())

    # See:
    # https://www.youtube.com/watch?v=hdkrWya61Ds
    for _ in range(q):
        ti, ki = map(int, input().split())
        ki -= 1
        si = 0

        if ti <= 60:
            b = 1 << ti
            si = ki // b
            ki %= b
    
        r = popcount(ki)
        l = ti - r
        x = l + (r * 2) + (ord(s[si]) - ord('A'))
        ans = chr(ord('A') + (x % 3))
        print(ans)


if __name__ == "__main__":
    main()
