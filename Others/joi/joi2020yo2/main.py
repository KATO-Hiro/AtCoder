# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    at = sorted([tuple(map(int, input().split())) for _ in range(n)])
    # print(at)

    # 往路/復路で分ける
    # 往路:
    # 地点0から最も離れているいちごの位置Amax
    # Amaxが熟した状態になる時刻t(Amax)の最大値
    outbound_trip = max(at[-1][0], at[-1][1])
    # print(outbound_trip)

    # 復路:
    # 右端から一つ左のいちごに移動 / 収穫できない場合は待機
    ans = outbound_trip
    pos = at[-1][0]

    for i in range(n - 2):
        ans += pos - at[i][0]
        ans = max(ans, at[i][1])

        pos = at[i][0]

    ans += pos

    print(ans)


if __name__ == "__main__":
    main()
