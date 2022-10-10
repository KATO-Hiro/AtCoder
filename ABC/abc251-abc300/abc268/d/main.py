# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    sys.setrecursionlimit(10 ** 8)
    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    t = defaultdict(int)

    for _ in range(m):
        ti = input().rstrip()
        t[ti] += 1
    
    remain = 16 - (n - 1)  # _を複数追加する回数

    for si in s:
        remain -= len(si)

    underscore = "_"
    used = [False] * n

    # ありうる文字列のパターンをDFSで全探索
    # 使用した文字の数、現在の文字列、_の残りの数
    def dfs(i: int, cur_s: str, underscore_count: int) -> bool:
        # 基本ケース
        if i == n:
            # コーナーケース: 3文字未満
            if len(list(cur_s)) < 3:
                return False
            
            if t[cur_s] != 0:
                return False
            
            print(cur_s)
            exit()
    
        # 再帰ケース
        if underscore_count > 0:
            if dfs(i, cur_s + underscore, underscore_count - 1):
                return True
        
        for j in range(n):
            if not used[j]:
                used[j] = True

                if dfs(i + 1, cur_s + underscore + s[j], underscore_count):
                    return True

                used[j] = False

        return False

    for i in range(n):
        used[i] = True
        dfs(1, s[i], remain)
        used[i] = False
    
    print(-1)


if __name__ == "__main__":
    main()
