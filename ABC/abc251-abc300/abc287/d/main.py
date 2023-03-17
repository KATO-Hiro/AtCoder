# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    s = input().rstrip()
    t = input().rstrip()
    m = len(t)
    ans = [True] * (m + 1)

    # 先頭と末尾の操作を共通化
    for _ in range(2):
        matched = True

        # 前処理: 先頭 / 末尾から文字列がマッチしているか1文字ずつ判定
        for i in range(m):
            if (s[i] != t[i] and s[i] != '?' and t[i] != '?'):
                matched = False
                
            if not matched:
                ans[i + 1] = False
        
        s, t, ans = s[::-1], t[::-1], ans[::-1]
    
    for ai in ans:
        if ai:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
