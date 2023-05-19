# -*- coding: utf-8 -*-


def main():
    import sys
    from functools import lru_cache

    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    # しりとりに使う単語(=状態)が少ないことを利用して、bitDP
    # ゲームは終局状態から考えるのが定石 + 再帰で表現

    # メモ化再帰をデコレータで表現
    @lru_cache(maxsize=None)
    def rec(word_set, prev_word):
        result = False

        for i in range(n):
            # i番目の単語を既に使っている
            if (word_set >> i) & 1:
                continue

            # しりとりができない
            if word_set != 0 and (s[i][0] != s[prev_word][-1]):
                continue

            result |= not rec(word_set | 1 << i, i)

        return result

    if rec(0, 0):  # 単語の集合、直前に使った単語
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
