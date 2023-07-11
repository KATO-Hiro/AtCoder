# -*- coding: utf-8 -*-


def main():
    import sys
    from math import gcd

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    front, back = [a[0]], [a[-1]]

    # 一つの要素を書き換え = 左右から累積的に演算して、後から合成
    for ai in a[1:]:
        front.append(gcd(ai, front[-1]))

    for ai in a[::-1][1:]:
        back.append(gcd(ai, back[-1]))

    back = back[::-1]

    ans = 1

    for i in range(n):
        if i == 0:
            candidate = back[i + 1]
        elif i == n - 1:
            candidate = front[i - 1]
        else:
            candidate = gcd(front[i - 1], back[i + 1])

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
