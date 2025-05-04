#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def

#main
def main():
    S = input()
    S = list(S)
    ans = []

    for ch in S:
        if ch.isupper():
            ans.append(ch)
    
    ans = ''.join(ans)
    print(ans)
    

if __name__ == '__main__':
    main()