# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    # しりとりに使う単語(=状態)が少ないことを利用して、bitDP
    # ゲームは終局状態から考えるのが定石 + 再帰で表現
    memo = [[False for _ in range(n)] for _ in range(1 << n)]
    results = [[False for _ in range(n)] for _ in range(1 << n)]

    def rec(word_set, prev_word):
        # 既に計算済みなら再利用
        if memo[word_set][prev_word]:
            return results[word_set][prev_word]

        result = False

        for i in range(n):
            # i番目の単語を既に使っている
            if (word_set >> i) & 1:
                continue

            # しりとりができない
            if word_set != 0 and (s[i][0] != s[prev_word][-1]):
                continue

            print(bin(word_set), word_set, i, s[i])

            result |= not rec(word_set | 1 << i, i)

        # メモを更新
        memo[word_set][prev_word] = True
        results[word_set][prev_word] = result

        return result

    if rec(0, 0):  # 単語の集合、直前に使った単語
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
