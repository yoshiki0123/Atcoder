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
    N = int(input())
    operations = []
    for _ in range(N):
        S = input()
        operations.append(S)
    
    ans = 0
    login_status = 0

    for operation in operations:
        if login_status == 0 and operation == 'login':
            login_status = 1
        elif login_status == 1 and operation == 'logout':
            login_status = 0
        elif login_status == 0 and operation == 'private':
            ans += 1
    
    print(ans)
    


if __name__ == '__main__':
    main()