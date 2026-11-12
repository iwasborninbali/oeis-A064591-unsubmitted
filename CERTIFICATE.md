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

Programs share no code or tables; the checker uses direct rational sums rather than the producer's closed form. The guide's review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6: `python3 programs/compute.py` found `[24, 112, 1984, 32512]` in both tests through 100000 and verified the even-factor identity; `python3 verification/check.py` found `[24, 112, 1984]` for all three tests through 5000 and printed `PASS`. Full logs are in `verification/logs/`.

## Not covered

The independent finite check does not cover the producer's full range. Neither open conjecture is proved or disproved. The proof is not formally machine-checked and uses Euclid–Euler for even perfect numbers. The source report's 5-million range and guide's 2-million range were not replayed.

## Guide's independent check

pending

## Verdict

partial — the independent finite check covers only 5000 rather than the producer's 100000 cases; the universal reduction is human-checkable only.
