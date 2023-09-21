# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    i_count = [0] * (w + 1)
    o_count = [0] * (h + 1)
    ans = 0

    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            match s[i][j]:
                case "J":
                    ans += i_count[j] * o_count[i]
                case "I":
                    i_count[j] += 1
                case "O":
                    o_count[i] += 1

    print(ans)


if __name__ == "__main__":
    main()
