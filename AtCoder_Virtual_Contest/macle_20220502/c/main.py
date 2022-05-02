# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod0 = 0
    modk_2 = 0

    # See:
    # https://blog.hamayanhamayan.com/entry/2018/09/02/225928
    for i in range(1, n + 1):
        if i % k == 0:
            mod0 += 1
    
    if k % 2 == 0:
        for i in range(1, n + 1):
            if i % k == k // 2:
                modk_2 += 1
        
    ans = mod0 ** 3 + modk_2 ** 3
    print(ans)


if __name__ == "__main__":
    main()
