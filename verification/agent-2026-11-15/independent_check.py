#!/usr/bin/env python3
"""Independent exhaustive check for A064591 through LIMIT.

No repository code is imported. The reciprocal expression is evaluated by a
weighted divisor sieve with exact INTEGER numerators: B(n) = n*(2*s0 - s1).
The ordinary and unitary divisor sums are computed independently via a
smallest-prime-factor sieve and prime-power products, not by a divisor sieve.
"""
import argparse
from array import array
from math import isqrt
from time import perf_counter


def run(limit):
    start = perf_counter()
    print(f"limit: {limit}", flush=True)

    # Compute B(n)=sum_{d|n} c(d)*(n/d), c(d)=2 (even) or -1 (odd).
    # This is mathematically equivalent to testing exact rational 2*s0-s1=1.
    balance = array('q', [0]) * (limit + 1)
    for divisor in range(1, limit + 1):
        w = 2 if divisor % 2 == 0 else -1
        k = 1
        for multiple in range(divisor, limit + 1, divisor):
            balance[multiple] += w * k
            k += 1
    t_balance = perf_counter()
    print(f"weighted-divisor-sieve seconds: {t_balance-start:.3f}", flush=True)

    # Factorization sieve (smallest prime factor); primes remain marked 0.
    spf = array('I', [0]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if not spf[p]:
            for j in range(p*p, limit+1, p):
                if not spf[j]:
                    spf[j] = p

    # From multiplicativity: sigma(p^e r)=sigma(r)*(1+...+p^e),
    # sigma_star(p^e r)=sigma_star(r)*(1+p^e), (r,p)=1.
    ordinary = array('Q', [0]) * (limit + 1)
    unitary = array('Q', [0]) * (limit + 1)
    ordinary[1] = unitary[1] = 1
    for n in range(2, limit + 1):
        p = spf[n]
        if p == 0:
            ordinary[n] = unitary[n] = n+1
        else:
            r = n
            power = 1
            while r % p == 0:
                r //= p
                power *= p
            ordinary[n] = ordinary[r] * ((power*p - 1)//(p-1))
            unitary[n] = unitary[r] * (1+power)
    t_factor = perf_counter()
    print(f"factorization-and-products seconds: {t_factor-t_balance:.3f}", flush=True)

    reciprocal = []
    nonunitary = []
    quadruple_perfect = []
    even_identity_failures = []
    mismatch_count = 0
    for n in range(1, limit+1):
        a = (n & -n).bit_length()-1
        m = n >> a
        r = (balance[n] == n)
        u = (ordinary[n]-unitary[n] == n)
        p = (n % 4 == 0 and ordinary[n//4] == n//2)
        if r:
            reciprocal.append(n)
        if u:
            nonunitary.append(n)
        if p:
            quadruple_perfect.append(n)
        if r != p or u != p:
            mismatch_count += 1
            if mismatch_count <= 10:
                print(f"MISMATCH n={n}: reciprocal={r} nonunitary={u} quadruple_perfect={p}")
        if a >= 1 and (ordinary[n]-unitary[n] !=
                (2**a - 2)*ordinary[m] +
                (2**a + 1)*(ordinary[m]-unitary[m])):
            if len(even_identity_failures) < 10:
                even_identity_failures.append(n)
    t_checked = perf_counter()
    print(f"comparison-and-identity seconds: {t_checked-t_factor:.3f}")
    print(f"reciprocal solutions: {reciprocal}")
    print(f"nonunitary perfect: {nonunitary}")
    print(f"four times perfect: {quadruple_perfect}")
    print(f"disagreements: {mismatch_count}")
    print(f"even identity failures (first ten): {even_identity_failures}")
    print(f"total seconds: {t_checked-start:.3f}")
    if mismatch_count or even_identity_failures:
        raise SystemExit("FAIL")
    print("PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=5_000_000)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("limit must be positive")
    run(args.limit)
