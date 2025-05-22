#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
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
    N, K = map(int,input().split())
    
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')

    print(N)


if __name__ == '__main__':
    main()