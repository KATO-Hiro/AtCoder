# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()

    # 例外処理
    if s.count("o") >= 5:
        print(0)
        exit()
    elif s.count("x") >= 7 and s.count("?") == 0:
        print(0)
        exit()

    ans = 0

    for i in range(10**4):
        i = str(i).zfill(4)
        c = Counter()

        for ii in i:
            c[int(ii)] += 1

        # print(c)
        flag = True

        for j, sj in enumerate(s):
            if sj == "o":
                if not (c[j] >= 1):
                    flag = False
                    break
            elif sj == "x":
                if not (c[j] == 0):
                    flag = False
                    break
            else:
                if not (c[j] >= 0):
                    flag = False
                    break

        if flag:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
