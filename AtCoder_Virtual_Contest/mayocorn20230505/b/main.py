# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    st = [tuple(map(str, input().split())) for _ in range(n)]

    for i, (si, ti) in enumerate(st):
        ok = list()

        for ai in [si, ti]:
            flag = True

            for j, (sj, tj) in enumerate(st):
                if i == j:
                    continue

                if ai == sj or ai == tj:
                    flag = False
                    break
    
            if flag:
                ok.append(True)
            else:
                ok.append(False)
        
        if ok.count(False) == 2:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
