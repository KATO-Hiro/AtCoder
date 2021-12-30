# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    mod = 10 ** 9 + 7
    xyzw = [list(map(int, input().split())) for _ in range(q)]
    ans = 1

    # See:
    # https://atcoder.jp/contests/typical90/submissions/24036175
    def is_ok(i, j):
        for x, y, z, w in xyzw:
            w1 = ((j >> x - 1) | (j >> y - 1) | (j >> z - 1)) & 1

            if w1 != ((w >> i) & 1):
                return False

        return True


    for i in range(60):
        count = 0

        for j in range(1 << n):
            if is_ok(i, j):
                count += 1
        ans *= count
        ans %= mod

    print(ans)
    

if __name__ == "__main__":
    main()
