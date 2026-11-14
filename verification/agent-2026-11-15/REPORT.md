# Independent verification — 2026-11-15

Basis: supplied archive `oeis-A064591-unsubmitted-150de51.zip`, commit `150de510a3e8079cdfd9aeacd5a040d1d23dd193`. Reviewed `README.md`, `CERTIFICATE.md`, `PRIOR-ART.md`, `proof.md`, both programs, and both existing logs. This report is independent of the repository's certificate; it is not a claim to have solved either open conjecture.

## Claim

**Exactly as asserted in `CERTIFICATE.md`:** For every integer `n >= 1`, `2*s0(n)-s1(n)=1` if and only if `n=4P` for an ordinary perfect number `P`; moreover Lagneau's equivalence `L` is logically equivalent to `W AND O`, where `W` is the Ligh–Wall classification of all nonunitary perfect numbers as four times **even** perfect numbers and `O` asserts that no odd perfect number exists.

## Proof check

**Referee assessment: correct with fixable gaps**, after the repairs below. Neither open conjecture is assumed true.

Line-by-line audit of `proof.md`:

- **Lines 3–4:** Definitions are standard; correct.
- **Lines 5–9:** For odd `n`, `s0=0` and `s1>0`; the displayed geometric sum for `n=2^a*m` is correct. No gap.
- **Lines 10–12:** `a=1` gives zero. For `a>=2`, the transformation to `t*sigma(m)=(t+1)*m` is reversible. No gap.
- **Line 14:** The cases `a=2` and `a>=3` are correct. From `gcd(t,t+1)=1`, `t|m`. Then `sigma(m)/m=sum_{d|m}1/d=1+1/t`. Both `1` and `t` divide `m`; positivity rules out any other divisor, forcing `m=t` and `t` prime. The converse is direct. No conjectural assumption.
