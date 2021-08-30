# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list()
    t = list()

    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    
    for i in range(n):
        count = 0
        si, ti = s[i], t[i]

        for j in range(i + 1, n):
            sj, tj = s[j], t[j]

            if si == sj and ti == tj:
                count += 1
        
        if count >= 1:
            print('Yes')
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
