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
    S1 = input()
    S2 = input()
    S3 = input()
    s = set((S1, S2, S3))
    full_s = set(('ABC' , 'ARC' , 'AGC' , 'AHC'))
    print(*(full_s - s))

if __name__ == '__main__':
    main()