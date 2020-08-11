# -*- coding: utf-8 -*-


def main():
    w_uni_score = sorted([int(input()) for _ in range(10)], reverse=True)
    k_uni_score = sorted([int(input()) for _ in range(10)], reverse=True)
    print(sum(w_uni_score[:3]), sum(k_uni_score[:3]))


if __name__ == '__main__':
    main()
