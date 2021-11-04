# -*- coding: utf-8 -*-


def main():
    from itertools import product
    n = int(input())

    patterns = product(range(2), repeat=n)
    ans = list()

    if n % 2 == 1:
        print()
        exit()

    for pattern in patterns:
        zero_count = 0
        one_count = 0
        ok = True
        candidate = ""

        for p in pattern:
            if p == 0:
                zero_count += 1
                candidate += "("
            else:
                one_count += 1
                candidate += ")"
            
            if zero_count > n // 2 or one_count > n // 2:
                ok = False
                break
            
            if zero_count < one_count:
                ok = False
                break
        
        if ok:
            ans.append(candidate)
    
    for a in sorted(ans):
        print(a)


if __name__ == "__main__":
    main()
