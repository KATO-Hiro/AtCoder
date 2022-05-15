# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = 0

    for i in range(0, 10 ** 4):
        t = list(str(i).zfill(4))
        count = [0] * 10

        for ti in t:
            count[int(ti)] += 1
        
        flag = True
        
        for j, si in enumerate(s):
            if si == "o" and count[j] == 0:
                flag = False
            elif si == "x" and count[j] >= 1:
                flag = False

        if flag:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
