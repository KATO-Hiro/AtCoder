# -*- coding: utf-8 -*-


def main():
    n = int(input())
    count = 0

    for i in range(n):
        si = input()

        if si == "A":
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                print("NO")
                exit()

    if count > 0:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
