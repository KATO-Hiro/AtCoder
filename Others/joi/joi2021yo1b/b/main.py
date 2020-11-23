# -*- coding: utf-8 -*-


def main():

    n = int(input())
    s = input()
    store = list()

    for si in s:
        if len(store) % 2 == 0 and si == "I":
            store.append(si)
        elif len(store) % 2 == 1 and si == "O":
            store.append(si)

        if len(store) == 3:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
