#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    N, K = map(int,input().split())
    village_money = []
    for _ in range(N):
        A, B = map(int,input().split())
        village_money.append((A, B))
    village_money = deque(sorted(village_money))

    cur_village = 0
    while K > 0 :
        cur_village += K
        K = 0

        for A, B in village_money:
            if A <= cur_village:
                K += B
                village_money.popleft()
            break
        
    print(cur_village)

if __name__ == '__main__':
    main()