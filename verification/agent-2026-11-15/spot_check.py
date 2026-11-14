#!/usr/bin/env python3
"""Direct divisor-by-divisor audit of the currently listed OEIS A064591 terms.

Works with large values by factoring their odd parts, then generating each
divisor, independently of either repository implementation or our bulk sieve.
"""
from fractions import Fraction
from math import gcd
from time import perf_counter

TERMS = (
    24,
    112,
    1984,
    32512,
    134201344,
    34359476224,
    549754765312,
    9223372032559808512,
)


def factor(n):
    result = []
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            exponent = 0
            while n % trial == 0:
                n //= trial
                exponent += 1
            result.append((trial, exponent))
        trial = 3 if trial == 2 else trial + 2
    if n > 1:
        result.append((n, 1))
    return result


def divisors(n):
    result = [1]
    for prime, exponent in factor(n):
        previous = tuple(result)
        ppower = 1
        for _ in range(exponent):
            ppower *= prime
            result.extend(d * ppower for d in previous)
    return sorted(result)


start = perf_counter()
for n in TERMS:
    d = divisors(n)
    sig = sum(d)
    u = sum(x for x in d if gcd(x, n // x) == 1)
    s0 = sum((Fraction(1, x) for x in d if x % 2 == 0), Fraction(0))
    s1 = sum((Fraction(1, x) for x in d if x % 2 != 0), Fraction(0))
    p = n // 4
    perfect = sum(divisors(p)) == 2*p
    ok = sig-u == n and 2*s0-s1 == 1 and perfect
    print(f"n={n} factors={factor(n)} divisors={len(d)} "
          f"sigma={sig} unitary={u} reciprocal={2*s0-s1} "
          f"four_times_perfect={perfect} result={'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("FAIL")
print(f"checked={len(TERMS)}; total seconds={perf_counter()-start:.3f}; PASS")
