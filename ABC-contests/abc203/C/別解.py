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
    AB = []
    for _ in range(N):
        AB.append(tuple(map(int,input().split())))
    AB.sort()
    
    cur_village = K
    for i in range(N):
        if cur_village < AB[i][0]:
            break
        cur_village += AB[i][1]
    print(cur_village)

if __name__ == '__main__':
    main()