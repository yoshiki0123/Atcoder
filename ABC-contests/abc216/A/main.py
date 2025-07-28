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
    X, Y = input().split('.')
    if 0 <= int(Y) <= 2:
        print(X+'-')
    elif 3 <= int(Y) <= 6:
        print(X)
    else:
        print(X+'+')
    
    

if __name__ == '__main__':
    main()