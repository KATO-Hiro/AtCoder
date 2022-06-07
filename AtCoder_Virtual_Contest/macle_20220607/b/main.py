# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = list()

    for x in range(10):
        for y in range(10):
            for z in range(10):
                ti = str(x) + str(y) + str(z)
                t.append(ti)

    ans = 0

    # 文字が一致したら、カーソルを進める
    for ti in t:
        cur = 0

        for si in s:
            if si == ti[cur]:
                cur += 1
            
            if cur == 3:
                break
        
        if cur == 3:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
