"""Direct divisor enumeration and rational sums, OpenAI Codex, 2026-11-13."""
from math import gcd,isqrt
from fractions import Fraction
N=5000
nu=[]; recip=[]; fourperfect=[]
for n in range(1,N+1):
    ds=set()
    for d in range(1,isqrt(n)+1):
        if n%d==0: ds.add(d); ds.add(n//d)
    sigma=sum(ds)
    unitary=sum(d for d in ds if gcd(d,n//d)==1)
    if sigma-unitary==n: nu.append(n)
    s0=sum((Fraction(1,d) for d in ds if d%2==0),Fraction())
    s1=sum((Fraction(1,d) for d in ds if d%2),Fraction())
    if 2*s0-s1==1: recip.append(n)
    if n%4==0:
        m=n//4
        pd=[d for d in range(1,isqrt(m)+1) if m%d==0]
        total=sum(d+(m//d if d*d!=m else 0) for d in pd)
        if total==2*m: fourperfect.append(n)
assert recip==fourperfect==nu
print('range:',N)
print('nonunitary perfect:',nu)
print('reciprocal equation:',recip)
print('four times perfect:',fourperfect)
print('PASS')
