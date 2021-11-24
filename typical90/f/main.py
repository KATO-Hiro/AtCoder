# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    alpha_size = 26
    c = [[0 for _ in range(n + 1)] for _ in range(alpha_size)]

    for i in range(alpha_size):
        c[i][n] = n

    for i in range(n - 1, -1, -1):
        for alpha in range(alpha_size):
            diff = ord(s[i]) - ord('a')

            if diff == alpha:
                c[alpha][i] = i
            else:
                c[alpha][i] = c[alpha][i + 1]
    
    cur_pos = 0
    ans = ""
    
    for i in range(1, k + 1):
        for j in range(alpha_size):
            next_pos = c[j][cur_pos]
            size = n - next_pos - 1 + i

            if size >= k:
                ans += chr(ord('a') + j)
                cur_pos = next_pos + 1
                break
    
    print(ans)


if __name__ == "__main__":
    main()
