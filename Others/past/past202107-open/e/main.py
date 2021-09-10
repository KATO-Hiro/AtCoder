# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for k in range(1, 31):
        x = 1

        for i in range(31):
            if i == k:
                x += 1
            else:
                x *= 3
            
            if x == n:
                print(k)
                exit()
    
    print(-1)


if __name__ == "__main__":
    main()
