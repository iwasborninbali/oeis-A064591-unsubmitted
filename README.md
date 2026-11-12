# OEIS A064591: reciprocal-divisor conjecture reduction (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 13 Nov 2026).

- [A064591](https://oeis.org/A064591), Lagneau's conjecture equivalent to Ligh-Wall plus no odd perfect numbers: **candidate** (2026-11-13: repository built (core c5)). Certificate: partial.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

A064591 lists positive integers n for which sigma(n)-sigma*(n)=n, in increasing order with offset 1. Here sigma sums all positive divisors and sigma* sums unitary divisors d satisfying gcd(d,n/d)=1. Let s₀ and s₁ be the sums of reciprocals of the even and odd divisors of n; the empty even-divisor sum is zero.

The snapshot `context/A064591.seq` and live [entry](https://oeis.org/A064591), read 2026-11-13, attribute to Michel Lagneau, January 21, 2015: “Conjecture: let s0 be the sum of the inverses of the even divisors of a number n and s1 the sum of the inverses of the odd divisors of n; then n is in the sequence iff 2*s0-s1 = 1.” The entry does not record the reduction.

## Terms / result

The reciprocal equation holds exactly when n is four times an ordinary perfect number, even or odd. Lagneau's conjecture is equivalent to the conjunction of the Ligh–Wall conjecture and the nonexistence of odd perfect numbers; it remains open.

| n | nonunitary perfect | reciprocal equation |
|---:|---|---|
| 24 | yes | yes |
| 112 | yes | yes |
| 1984 | yes | yes |
| 32512 | yes | yes |

## How it was obtained

Writing n=2^a m with m odd makes the reciprocal equation a sharp equality for sigma(m)/m. A second identity expresses the difference from nonunitary perfection; it yields the exact logical equivalence. See [proof.md](proof.md).

## Verification

The producer checks the two conditions through 100000; an independently written divisor and rational-arithmetic checker compares both and the four-times-perfect condition through 5000. The proof is human-checkable, not machine-checked; finite agreement does not settle the conjecture. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Lagneau stated the conjecture; Ligh and Wall stated the nonunitary-perfect classification and proved one direction. ChatGPT derived the reduction; Claude Code reviewed it. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 programs/compute.py` and `python3 verification/check.py`, together under a second on the recorded machine. The former finds 24, 112, 1984, 32512 through 100000; the latter finds 24, 112, 1984 through 5000 and ends `PASS`. Complete logs are in `verification/logs/`.

## Provenance

Source `projects/science/athanor-oeis`, commit `7662d9a678c6d414685a899a631c63ac320f6840`, paths `tasks/2026-11-12-A064591-nonunitary-perfect-inverses/answers/2026-11-12-chatgpt.md`, `context/A064591.seq`, and `TASK.md`. Guide review is recorded in `tasks/README.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
