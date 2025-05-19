#library
import sys, re, heapq
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    H, W, N = map(int,input().split())
    rows = [[] for _ in range(H)]
    cols = [[] for _ in range(W)]
    rows_count = [0] * H
    cols_count = [0] * W


    for _ in range(N):
        X, Y = map(int,input().split())
        X, Y = X-1, Y-1
        rows[X].append(Y)
        cols[Y].append(X)
        rows_count[X] += 1
        cols_count[Y] += 1
    
    Q = int(input())
    for _ in range(Q):
        query = list(map(int,input().split(' ')))
        if query[0] == 1:
            x = query[1] - 1
            print(rows_count[x])
            if rows_count[x] == 0:              
                continue
            rows_count[x] = 0
            for y in rows[x]:
                if cols_count[y] > 0:
                    cols_count[y] -= 1

        else:
            y = query[1] - 1
            print(cols_count[y])
            if cols_count[y] == 0: 
                continue
            cols_count[y] = 0
            for x in cols[y]:
                if rows_count[x] > 0:
                    rows_count[x] -= 1

if __name__ == '__main__':
    main()