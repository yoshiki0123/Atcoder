#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    S = input()
    S = set(S)

    for i in range(26):
        if chr(ord('a') + i) not in S:
            print(chr(ord('a') + i))
            exit()

if __name__ == '__main__':
    main()