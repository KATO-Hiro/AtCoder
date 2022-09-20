# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    s = bin(int(input()))[2:]
    m = len(s)
    flag_id = list()

    for i, si in enumerate(s):
        if si == '1':
            flag_id.append(i)
    
    size = len(flag_id)
    bools = product([True, False], repeat=size)
    ans = list()

    for bool in bools:
        value = ["0"] * m 

        for b, i in zip(bool, flag_id):
            if b:
                value[i] = "1"
        
        ans.append(int(''.join(map(str, value)), 2))
    
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
