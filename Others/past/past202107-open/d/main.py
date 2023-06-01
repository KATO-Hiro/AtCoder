# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())

    # 指定された文字の構造: [aiueo]のどれか + x + [aiueo]のどれか
    for i in range(1, n - 1):
        if s[i] == "x" and s[i - 1] == s[i + 1] and s[i - 1] in "aiueo":
            s[i - 1] = "."
            s[i] = "."
            s[i + 1] = "."

    print("".join(s))


if __name__ == "__main__":
    main()
