# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    p = int(input())
    coin  = 1

    for i in range(1, 11):
        coin *= i
    
    ans = 0
    
    for i in range(10, 0, -1):
        count = min(100, p // coin)
        ans += count
        p -= count * coin
        coin //= i
    
    print(ans)



if __name__ == "__main__":
    main()
