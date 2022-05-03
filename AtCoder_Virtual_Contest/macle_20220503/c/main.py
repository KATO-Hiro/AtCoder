# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    honests = defaultdict(list)
    liars = defaultdict(list)

    for i in range(n):
        ai = int(input())

        for j in range(ai):
            xi, yi = map(int, input().split())

            if yi== 0:
                liars[i].append(xi - 1)
            else:
                honests[i].append(xi - 1)

    ans = 0
    
    for mask in range(1 << n):
        count = 0
        is_ok = True

        for j in range(n):
            if mask & (1 << j):
                count += 1    

                for honest in honests[j]:
                    if not (mask & (1 << honest)):
                        is_ok = False
                        break
                
                for liar in liars[j]:
                    if mask & (1 << liar):
                        is_ok = False
                        break
        
        if is_ok:
            ans = max(ans, count)
    
    print(ans)


if __name__ == "__main__":
    main()
