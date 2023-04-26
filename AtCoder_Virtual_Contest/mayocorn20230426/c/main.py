# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    h1_patterns = list(product([0, 1], repeat=h1))
    w1_patterns = list(product([0, 1], repeat=w1))

    for h1_pattern in h1_patterns:
        if sum(h1_pattern) != h2:
            continue
    
        c = list()

        for i, ai in enumerate(a):
            if h1_pattern[i] == 1:
                c.append(ai)

        for w1_pattern in w1_patterns:
            if sum(w1_pattern) != w2:
                continue

            d = list()
        
            for ci in c:
                e = list()

                for ck, wi in zip(ci, w1_pattern):
                    if wi == 1:
                        e.append(ck)
                
                d.append(e)
            
            if d == b:
                print("Yes")
                exit()
    
    print("No")


if __name__ == "__main__":
    main()
