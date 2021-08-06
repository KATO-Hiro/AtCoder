# -*- coding: utf-8 -*-


def main():
    x = list(input())

    is_weak = True

    for i in range(3):
        if (int(x[i]) + 1) % 10 != int(x[i + 1]):
            is_weak = False

    if len(set(x)) == 1:
        print("Weak")
    elif is_weak:
        print("Weak")
    else:
        print("Strong")



if __name__ == "__main__":
    main()
