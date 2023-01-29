# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    
    for j in range(1, n):
        count = 0
        is_print = False

        for i in range(n):
            k = i + j

            if k >= n:
                continue

            if s[i] != s[k]:
                count += 1
            else:
                print(count)
                is_print = True

                break
    
        if not is_print:
            print(count)
    

if __name__ == "__main__":
    main()
