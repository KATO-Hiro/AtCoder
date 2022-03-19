# -*- coding: utf-8 -*-




def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = list()
    numbers = list()

    for i in range(1, int(sqrt(m)) + 1):
        if m % i == 0:
            numbers.append(i)
            numbers.append(m // i)
        
    for number in numbers:
        if m % number == 0 and m // number >= n:
            ans.append(number)
    
    print(max(ans))


if __name__ == "__main__":
    main()
