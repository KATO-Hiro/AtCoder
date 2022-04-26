# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    from collections import Counter
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    n = len(s)
    c = Counter(s)
    numbers = ""

    if n == 1:
        if int(*s) == 8:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    
    if n == 2:
        if int(''.join(map(str, s))) % 8 == 0 or int(''.join(map(str, s[::-1]))) % 8 == 0:
            print("Yes")
            exit()
        else:
            print("No")
            exit()

    for key, value in c.items():
        size = min(3, int(value))
        numbers += key * size

    for number in permutations(numbers, 3):
        if int(''.join(map(str, number))) % 8 == 0:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
