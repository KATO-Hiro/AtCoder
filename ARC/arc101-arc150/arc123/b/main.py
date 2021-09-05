# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    used_b = [False] * n
    used_c = [False] * n
    ans = 0
    old_j = 0
    old_k = 0

    for i, ai in enumerate(a):
        b_flag = False
        c_flag = False

        j = old_j

        while j < n:
            if not used_b[j] and ai < b[j]:
                b_flag = True
                used_b[j] = True
                break

            j += 1
        
        k = old_k

        while j < n and k < n:
            if not used_c[k] and b[j] < c[k]:
                c_flag = True
                used_c[k] = True
                break

            k += 1
        
        if b_flag and c_flag:
            ans += 1
        
        old_j = j
        old_k = k

    print(ans)


if __name__ == "__main__":
    main()
