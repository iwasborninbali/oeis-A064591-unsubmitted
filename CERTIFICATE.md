# Verification certificate

## Claim

For n>=1, 2s₀(n)-s₁(n)=1 iff n is four times an ordinary perfect number.

Lagneau's conjecture is equivalent to the Ligh–Wall conjecture together with nonexistence of odd perfect numbers.

## Evidence

| What | Program | Author and date | Coverage | Result |
|---|---|---|---|---|
| Human-checkable proof | `proof.md` | Adapted by OpenAI Codex from ChatGPT, 2026-11-12 | Both universal equivalences | Not machine-checked |
| Producer | `programs/compute.py` | OpenAI Codex, 2026-11-13 | Divisor-sum sieve and factor identity through 100000 | Passed |
| Independent check | `verification/check.py` | OpenAI Codex, 2026-11-13 | Direct divisors, rational reciprocal sums, and perfect numbers through 5000 | Passed |
| Independent referee and check | `verification/agent-2026-11-15/` (REPORT.md, independent_check.py, spot_check.py) | ChatGPT agent, 2026-11-15; own code, no repository code | Reciprocal equation and nonunitary perfect numbers through 5,000,000; the eight displayed terms checked directly; proof read line by line | Passed; proof correct with one omitted standard lemma |

Programs share no code or tables; the checker uses direct rational sums rather than the producer's closed form. The guide's review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6: `python3 programs/compute.py` found `[24, 112, 1984, 32512]` in both tests through 100000 and verified the even-factor identity; `python3 verification/check.py` found `[24, 112, 1984]` for all three tests through 5000 and printed `PASS`. Full logs are in `verification/logs/`.

2026-11-15, Darwin arm64, Python 3.14.6, by the guide: `python3 independent_check.py --limit 5000000` and
`python3 spot_check.py` in `verification/agent-2026-11-15/` passed (0 disagreements; four solutions 24, 112, 1984,
32512 below the limit).

## Not covered

The independent finite check does not cover the producer's full range. Neither open conjecture is proved or disproved. The proof is not formally machine-checked and uses Euclid–Euler for even perfect numbers. The source report's 5-million range and guide's 2-million range were not replayed.

## Guide's independent check

15 November 2026: the guide read `proof.md` line by line. For n = 2^a m, s1 = sigma(m)/m and s0 = (1 - 2^-a) sigma(m)/m;
for a >= 2 the equation becomes t sigma(m) = (t+1) m with t = 2^(a-1) - 1; a = 2 gives odd perfect m; for a >= 3,
gcd(t, t+1) = 1 forces t | m and then sigma(m)/m = 1 + 1/t forces m = t prime, i.e. four times an even perfect number
(the standard fact that 2^p - 1 prime implies p prime, omitted in the text, is noted by the referee). Identity (2)
follows from sigma(2^a m) = (2^(a+1) - 1) sigma(m) and sigma*(2^a m) = (2^a + 1) sigma*(m). The step L => O uses that an
odd perfect number is not squarefree (sigma of a squarefree m with two odd primes is divisible by 4). Verdict: correct.

## Verdict

complete — the classification of 2 s0 - s1 = 1 and the equivalence of Lagneau's statement with Ligh-Wall plus no odd
perfect numbers are proved (read independently by the guide and by a separate referee); computations are reproduced
by programs that share no code. Not covered: no formal proof; neither open conjecture is resolved.
