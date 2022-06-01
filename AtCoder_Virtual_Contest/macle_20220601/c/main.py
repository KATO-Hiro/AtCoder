# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s_dash = input().rstrip()
    t = input().rstrip()
    n = len(s_dash)
    m = len(t)
    candidates = list()

    for i in range(n - m + 1):
        si_dash = s_dash[i:i + m]
        flag = True

        for sii_dash, ti in zip(si_dash, t):
            if sii_dash == "?" or sii_dash == ti:
                pass
            else:
                flag = False
        
        if not flag:
            continue

        u = s_dash[:i] + t + s_dash[i + m:]
        candidates.append(u.replace('?', 'a'))
    
    if len(candidates) == 0:
        print("UNRESTORABLE")
    else:
        print(sorted(candidates)[0])


if __name__ == "__main__":
    main()
