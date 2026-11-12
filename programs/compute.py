"""Divisor-sum sieve, OpenAI Codex, 2026-11-13."""
from math import gcd
N=100000
sigma=[0]*(N+1); unitary=[0]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d):
        sigma[n]+=d
        if gcd(d,n//d)==1: unitary[n]+=d
nonunit=[n for n in range(1,N+1) if sigma[n]-unitary[n]==n]
recip=[]
for n in range(2,N+1,2):
    a=(n & -n).bit_length()-1; m=n>>a
    assert sigma[n]-unitary[n] == (2**a-2)*sigma[m]+(2**a+1)*(sigma[m]-unitary[m])
    if (2**a-2)*sigma[m]==n: recip.append(n)
print('range:',N)
print('nonunitary perfect:',nonunit)
print('reciprocal equation:',recip)
print('even-factor identity: PASS')
assert nonunit==recip
