# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [input().rstrip()[3:] for _ in range(n)]
    t = [input().rstrip() for _ in range(m)]
    ans = 0

    for si in s:
        count = 0

        for ti in t:
            if ti in si:
                count += 1
        
        if count >= 1:
            ans += 1
    
    print(ans)
    

if __name__ == "__main__":
    main()
