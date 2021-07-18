# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d = dict()
    ans = list()
    
    for i in range(n):
        s = input()

        if s not in d.keys():
            d[s] = 1
            ans.append(i + 1)
            
    for a in ans:
        print(a) 


if __name__ == "__main__":
    main()
