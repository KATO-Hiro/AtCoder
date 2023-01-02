# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    left_count = 0
    right_count = 0
    left_index = list()
    d = dict()

    for i, si in enumerate(s):
        if si == "(":
            left_count += 1
            left_index.append(i)
        elif si == ")":
            right_count += 1

            left = 0
            right = i

            if left_count > right_count:
                left = left_index[-(right_count + 1)] + 1
            
            for key, value in list(d.items()):
                if left < value < right:
                    del d[key]
        else:
            if si not in d.keys():
                d[si] = i
            else:
                print("No")
                exit()
    
    print("Yes")
    

if __name__ == "__main__":
    main()
