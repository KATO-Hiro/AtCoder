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
    
    for size in range(3, 7 + 1):
        for i in range(7 - size + 1):
            ok = True
            q = p[i:i + size]

            for j in range(size):
                if j == 0 or j == size - 1:
                    if q[j] == 0:
                        ok = False
                else:
                    if q[j] > 0:
                        ok = False
        
            if ok:
                print("Yes")
                exit()
        
    print("No")


if __name__ == "__main__":
    main()
