# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    q = int(input())
    ans = list()

    # シンプルな順列を考える
    # ri + ci > nのとき黒マスになることに気が付けるか?
    # 複雑なケースも、行 / 列を入れ替えただけと考える
    for i in range(q):
        ri, ci = map(int, input().split())
        ri -= 1
        ci -= 1

        if (r[ri] + c[ci]) > n:
            ans.append("#")
        else:
            ans.append(".")
    
    print("".join(ans))



if __name__ == "__main__":
    main()
