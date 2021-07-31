# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()

    for i, si in enumerate(s):
        if si =='1':
            if i % 2 == 0:
                print("Takahashi")
                exit()
            else:
                print("Aoki")
                exit()
        


if __name__ == "__main__":
    main()
