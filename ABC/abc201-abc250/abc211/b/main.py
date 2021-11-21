# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    c = Counter()

    for _ in range(4):
        s = input()
        c[s] += 1

    if len(c) == 4:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
