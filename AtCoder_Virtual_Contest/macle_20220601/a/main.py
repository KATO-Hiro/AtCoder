# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    value = 0
    ans = 1

    for i in range(1, n + 1):
        candidate = i
        count = 0

        while True:
            if i % 2 == 0:
                i //= 2
                count += 1
            else:
                break
        
        if count > value:
            value = count
            ans = candidate
    
    print(ans)


if __name__ == "__main__":
    main()
