# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    st = [list(map(str, input().rstrip().split())) for _ in range(n)]

    for i in range(n):
        ok = [True] * 2

        for k, ai in enumerate(st[i]):
            count = 0

            for j in range(n):
                if i == j:
                    continue

                if st[j][0] != ai and st[j][1] != ai:
                    count += 1
            
            if count != n - 1:
                ok[k] = False
        
        if ok == [False] * 2:
            print("No")
            exit()
    
    print("Yes")


if __name__ == "__main__":
    main()
