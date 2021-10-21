# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    s2 = s + s
    candidates = set()

    for i in range(n):
        t = s2[i:i + n]
        candidates.add(t)
    
    print(min(candidates))
    print(max(candidates))
    

if __name__ == "__main__":
    main()
