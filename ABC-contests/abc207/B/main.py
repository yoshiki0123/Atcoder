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
    A, B, C, D = map(int,input().split())
    if C*D <= B:
        print(-1)
    else:
        print(ceil(A / (C*D - B)))

    
if __name__ == '__main__':
    main()