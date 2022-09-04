# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    p = [0] * 7
    t = {6:0, 3:1, 1:2, 7:2, 0:3, 4:3, 2:4, 8:4, 5:5, 9:6}

    if s[0] == "1":
        print("No")
        exit()

    for i, si in enumerate(s):
        j = t[i]

        if si == "1":
            p[j] += 1
    
    # 10...01の形式になっているか3重ループで判定
    for i in range(7):
        for j in range(i + 2, 7):
            ok = True

            if p[i] >= 1 and p[j] >= 1:
                for k in range(i + 1, j):
                    if p[k] > 0:
                        ok = False
            else:
                ok = False

            if ok:
                print("Yes")
                exit()
        
    print("No")


if __name__ == "__main__":
    main()
