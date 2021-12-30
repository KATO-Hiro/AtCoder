# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    mod = 10 ** 9 + 7
    x, y, z, w = [0] * 100, [0] * 100, [0] * 100, [0] * 100
    nx, ny, nz, nw = [0] * 100, [0] * 100, [0] * 100, [0] * 100
    ans = 1

    for i in range(q):
        xi, yi, zi, wi = map(int, input().split())
        x[i], y[i], z[i], w[i] = xi - 1, yi - 1, zi - 1, wi
    
    def brute_force_search():
        count = 0

        for i in range(1 << n):
            bit = [0] * (n + 3)

            for j in range(n):
                bit[j] = (i // (1 << j)) % 2
            
            flag = True

            for k in range(q):
                if bit[nx[k]] | bit[ny[k]] | bit[nz[k]] != nw[k]:
                    flag = False
                    break

            if flag:
                count += 1
        
        return count


    for i in range(60):
        for j in range(q):
            nx[j], ny[j], nz[j] = x[j], y[j], z[j]
            nw[j] = (w[j] // (1 << i)) % 2
        
        count = brute_force_search()
        ans *= count
        ans %= mod

    print(ans)
    

if __name__ == "__main__":
    main()
