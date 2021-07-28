# -*- coding: utf-8 -*-


def lcm(a: int, b: int) -> int:
    '''Compute least common multiple of a and b.
    Args:
        a: Int of number (greater than 0).
        b: Int of number (greater than 0).
    Returns:
        least common multiple.
    Landau notation: O(log n)
    See:
    https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
    https://docs.python.org/3/library/sys.html#sys.version_info
    '''

    from math import gcd

    return a * b // gcd(a, b)


# See:
# https://blog.hamayanhamayan.com/entry/2020/01/11/145024
def naive(n, m, b):
    ans = 0
    
    for i in range(m):
        ok = True

        for j in range(n):
            # 各数字が(ak / 2)で割り切れない
            if i % b[j] != 0:
                ok = False
            # 2p + 1が偶数になる
            if (i // b[j]) % 2 == 0:
                ok = False
            
            if ok:
                print(i)
                ans += 1
    
    return ans


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0 for _ in range(n)]

    for index, ai in enumerate(a):
        if ai % 2 == 0:
            b[index] = ai // 2
        else:
            print(0)
            exit()
    
    l = b[0]

    for bi in b[1:]:
        l = lcm(l, bi)
    
    # 2p + 1が偶数になるかどうかをチェック
    for bi in b:
        if (l // bi) % 2 == 0:
            print(0)
            exit()

    count = m // l
    print(ceil(count / 2))


    # print(naive(n, m, b))


if __name__ == "__main__":
    main()
