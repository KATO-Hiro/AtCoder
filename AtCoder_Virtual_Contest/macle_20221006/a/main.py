# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    d = defaultdict(int)

    for si in s:
        if si[0] == "!" and si[1:] in d.keys():
            print(si[1:])
            exit()
        else:
            if ("!" + si) in d.keys():
                print(si)
                exit()
    
        d[si] += 1


    print("satisfiable") 


if __name__ == "__main__":
    main()
