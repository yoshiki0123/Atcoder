#library
import sys, re, heapq
from math import (
sin, cos, radians, ceil, 
floor, sqrt, isqrt, pi, 
gcd, comb, factorial
)
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
    N, X = map(int,input().split())
    A = list(map(int, input().split(' ')))
    if X >= sum(A) - N // 2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()