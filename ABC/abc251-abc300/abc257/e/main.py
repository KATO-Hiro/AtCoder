# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = list(map(int, input().split()))[::-1]

    # xの最大値 → 桁数をなるべく多く、先頭の桁ほど値が大きくする
    # 桁数の上限
    c_min = min(c)
    digit_max = n // c_min
    digit = digit_max

    ans = list()

    # 先頭の桁から条件を満たすように構築
    # コストciを払ったときに、最大の桁数が維持されるかどうか?
    for d in range(digit_max):
        for i, ci in enumerate(c):
            j = 9 - i

            if (n - ci) >= (digit - 1) * c_min:
                ans.append(str(j))
                n -= ci
                break
        
        digit -= 1
    
    print(''.join(ans))


if __name__ == "__main__":
    main()
