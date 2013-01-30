"""
Author: Eric Chio
Contact: im.ckieric@gmail.com
Initial commit date: 1/28/2013

Original Problem Statement:

After sending smileys, John decided to play with arrays. Did you know that hackers enjoy playing with arrays? John has a zero-based index array, m, which contains n non-negative integers. However, only the first k values of the array are known to him, and he wants to figure out the rest.

John knows the following: for each index i, where k <= i < n, m[i] is the minimum non-negative integer which is *not* contained in the previous *k* values of m.

For example, if k = 3, n = 4 and the known values of m are [2, 3, 0], he can figure out that m[3] = 1.

John is very busy making the world more open and connected, as such, he doesn't have time to figure out the rest of the array. It is your task to help him.

Given the first k values of m, calculate the nth value of this array. (i.e. m[n - 1]).

Because the values of n and k can be very large, we use a pseudo-random number generator to calculate the first k values of m. Given non-negative integers a, b, c and positive integer r, the known values of m can be calculated as follows:

m[0] = a
m[i] = (b * m[i - 1] + c) % r, 0 < i < k
Input
The first line contains an integer T (T <= 20), the number of test cases.
This is followed by T test cases, consisting of 2 lines each.
The first line of each test case contains 2 space separated integers, n, k (1 <= k <= 105, k < n <= 109).
The second line of each test case contains 4 space separated integers a, b, c, r (0 <= a, b, c <= 109, 1 <= r <= 109).
Output
For each test case, output a single line containing the case number and the nth element of m.


Problem:
Return the n'th char the unknown sequence.

Solution:
Observations:
- Anything like O(n), O(n * log k) is going to run too long
- You can't really generate that long sequence
- When a modulo is included, it implicates a recurring sequence or a period

INPUT:
5
97 39
34 37 656 97
186 75
68 16 539 186
137 49
48 17 461 137
98 59
6 30 524 98
46 18
7 11 9 46

OUTPUT
Case #1: 8
Case #2: 38
Case #3: 41
Case #4: 40
Case #5: 12
"""

import heapq

BIG_NUMBER = 100000000000

def gen(k, a, b, c, r):
    m = [a]
    for i in xrange(k-1):
        t = (b * m[i] + c) % r
        m.append(t)
    return m

def get_k_seq(seq, k):
    exists = {}
    seq_len = len(seq) 
    for i in xrange(seq_len):
        exists[seq[i]] = i

    pre_k_seq = sorted(set(xrange(k+1)) - set(seq))
    candidates = sorted(set(xrange(k+1)) - set(pre_k_seq))
    
    k_seq = []
    k_idx = 0

    while len(pre_k_seq) > 0 and len(candidates) > 0:
        candidate = filter(lambda x: exists[x] < k_idx + seq_len - k , candidates)
        if len(candidate) > 0:
            candidate = candidate[0]
        else:
            candidate = BIG_NUMBER
        
        if candidate > pre_k_seq[0]:
            k_seq.append(pre_k_seq[0])
            pre_k_seq = pre_k_seq[1:]            
        else:
            k_seq.append(candidate)
            candidates.remove(candidate)
        k_idx += 1
    
    while len(candidates) > 0:        
        k_seq.append(candidates[0])
        candidates.remove(candidates[0])
        
    while len(pre_k_seq) > 0:
        k_seq.append(pre_k_seq[0])
        pre_k_seq = pre_k_seq[1:]

    return k_seq
    
def s(n, k, a, b, c, r):
    seq = gen(k, a, b, c, r)

    pos = (n % (k+1)) + k
    k_seq = get_k_seq(seq, k)
    pos = pos-k
    
    return k_seq[pos]
    
input = [[46,18,7,11,9,46], \
[112,73,1,5,3,64100], \
[45068754,29153,2,9,5,999904402], \
[497151700,96511,9,7,6,999919625], \
[66,39,35,2,589,66], \
[977365070,59489,8,5,9,999966210], \
[22,21,1,4,869,22], \
[693840425,90561,2,6,7,999957328], \
[640834505,28785,3,9,1,999946125], \
[840698758,13331,8,7,10,999955808], \
[1000000000,100000,999999999,1,999999999,1000000000], \
[198,81,8,5,7,83495], \
[1000000000,100000,1,1,1,1000000000], \
[73,26,5,8,4,54214], \
[220,88,1,8,3,58265], \
[1000000000,100000,100000,1,0,1000000000], \
[1000000000,1,12,7,74,12], \
[97,39,34,37,656,97], \
[1000000000,100000,1,1,0,2], \
[98,59,6,30,524,98]]

for idx, i in enumerate(input):
    print 'Case #%d: %s' % (idx+1, s(i[0], i[1], i[2], i[3], i[4], i[5]))