# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    last_time, last_count = [-1] * n, [-1] * n
    cur_time, cur_count = 0, 0 

    while True:
        if cur_time == k:
            print(cur_count)
            exit()
        
        mod_n = cur_count % n
        
        if last_time[mod_n] != -1:
            break
        
        last_time[mod_n] = cur_time
        last_count[mod_n] = cur_count
        cur_time += 1
        cur_count += a[mod_n]
    
    cycle = (k - cur_time) // (cur_time - last_time[cur_count % n])
    next_time = cur_time + cycle * (cur_time - last_time[cur_count % n])
    next_count = cur_count + cycle * (cur_count - last_count[cur_count % n])

    while next_time < k:
        next_count += a[next_count % n]
        next_time += 1
    
    print(next_count)


if __name__ == "__main__":
    main()
