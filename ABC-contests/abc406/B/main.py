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
    A_list = list(map(int, input().split(' ')))
    
    ans = 1
    for A in A_list:
        ans *= A

        if len(str(ans)) > K:
            ans = 1
    
    print(ans)

if __name__ == '__main__':
    main()