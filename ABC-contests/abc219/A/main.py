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
    X = int(input())
    if X >= 90:
        print('expert')
        exit()
    else:
        if X < 40:
            print(40-X)
        elif X < 70:
            print(70-X)
        else:
            print(90-X)
    

if __name__ == '__main__':
    main()