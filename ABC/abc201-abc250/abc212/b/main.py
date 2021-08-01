# -*- coding: utf-8 -*-


def main():
    x = list(input())
    count = 0

    for j in range(3):
        if 0 <= int(x[j]) <= 8 and int(x[j + 1]) == int(x[j]) + 1:
            count += 1
        elif int(x[j]) == 9 and int(x[j + 1]) == 0:
            count += 1

    if len(set(x)) == 1:
        print("Weak")
    elif count == 3:
        print("Weak")
    else:
        print("Strong")

if __name__ == "__main__":
    main()
