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
- **Lines 15–16:** The Euclid–Euler step is correct but silently uses the elementary fact that if `2^p-1` is prime, then `p` is prime. **Fixable omitted lemma:** if `p=uv` with `u,v>1`, then `2^u-1` is a proper divisor of `2^p-1`. With this sentence supplied, the even-perfect classification follows; the `a=2` case supplies the four-times-odd-perfect numbers. No fatal gap.
- **Lines 18–22:** Multiplicativity gives `sigma(2^a*m)=(2^(a+1)-1)*sigma(m)` and `sigma_star(2^a*m)=(2^a+1)*sigma_star(m)`. Their difference is exactly identity (2). No gap.
- **Line 24:** Nonnegativity and the criterion `sigma(m)=sigma_star(m)` iff `m` is squarefree are correct; hence the equality statement for even nonunitary perfect `n` is correct. No gap.
- **Lines 26–27:** Logical definitions of `L`, `W`, `O` are appropriate. No gap.
- **Line 28:** The unqualified assertion **"if it has at least two distinct odd prime factors, sigma(m) is divisible by 4" is false**. For example `m=45=3^2*5` has two distinct odd prime factors but `sigma(45)=78`, not divisible by four. **Fixable and essential qualification:** *suppose for contradiction that the hypothetical odd perfect `m` is squarefree*. If it has at least two prime factors, `sigma(m)=product_{p|m}(1+p)` is divisible by four, whereas `2m` is not. If it has one, it is an odd prime with `sigma(m)=m+1<2m`; `m=1` is not perfect. Thus an odd perfect `m` cannot be squarefree. Identity (2) at `n=4m` then gives `sigma(n)-sigma_star(n)=n+5*(sigma(m)-sigma_star(m))>n`, contradicting `L`. This repairs the proof of `L => O`. The gap is not fatal to the claimed theorem.
- **Lines 28–30 (remaining):** With `O` established, the reciprocal classification and `L` imply `W`. Conversely `W AND O` implies `L`. These are sound purely logical implications. Ligh–Wall's proven forward inclusion is not used as an unproved converse. No unresolved conjecture is treated as a lemma.

**Independent mathematical conclusion:** Both universal equivalences are true with the two explicit minor proof repairs above. The currently committed prose should be corrected before presenting it as a finished proof, but the claim does not depend on the truth of `W` or `O`.

## Independent computation

Two Python 3 programs in this directory were independently written from scratch, importing no repository code or tables:

1. `independent_check.py`: exact weighted-divisor sieve computes the integer `B(n)=n*(2*s0(n)-s1(n))=sum_{d|n}(2 if d even else -1)*(n/d)` for **all `1 <= n <= 5,000,000`**; a separately implemented smallest-prime-factor sieve and prime-power multiplicative products compute `sigma(n)` and `sigma_star(n)`. It compares `B(n)=n`, `sigma(n)-sigma_star(n)=n`, and `4|n AND sigma(n/4)=n/2` for *every* `n`, and checks identity (2) independently for every even `n`. This is 1,000 times the existing 5,000-element independent check and 50 times the producer's 100,000-element range. Output: **all three lists `[24, 112, 1984, 32512]`, zero disagreements, zero identity failures, PASS**. Script's wall timer: **23.961 seconds** (outer `/usr/bin/time`: 32.63 seconds wall, 31.77 seconds user CPU, approximately 232 MB peak RSS). Log: `output.log`.
2. `spot_check.py`: separately generates individual divisors by trial factorization and checks `sigma`, `sigma_star` via gcd, and the reciprocal condition using exact `fractions.Fraction`; also directly tests whether `n/4` is ordinary perfect. Checks all **eight currently displayed OEIS terms**, including `134201344`, `34359476224`, `549754765312`, and `9223372032559808512`, individually beyond the sieve bound. Output: **8/8 PASS**, 0.008 seconds reported, `spot-check.log`. This is a witness check only, not an exhaustive exclusion of other values above 5 million.

Exact SHA-256 hashes of local scripts and captured output bytes:

| File | SHA-256 |
|---|---|
| `independent_check.py` | `f6c22aa17ddde3c96cc93cf8653a2146db8c07cdd2bf37056e0caee135a7599d` |
| `output.log` | `c32becb5721d7a101a5e6e73c842f0b28fe10d5172f36c767e28d1f407d598a2` |
| `spot_check.py` | `7c062501340e300ea38f7ca83adc5f20fd2c476d71c68aadbe5ba88408aff906` |
| `spot-check.log` | `eec253f3d09565dfb6f6c807798c3b76bb44ae999b241803149916ba928cc588` |

Reproduce with `python3 verification/agent-2026-11-15/independent_check.py --limit 5000000` and `python3 verification/agent-2026-11-15/spot_check.py` at the repository root. Finite computation is supporting evidence; universal truth comes from the repaired argument.

## Prior art

Search date 2026-11-15. Priority is **not established**: a targeted search cannot prove that no earlier equivalent derivation exists. Sources and negative searches:

