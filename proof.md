# Proof of the reduction

Let sigma(n) be the sum of divisors of n, and sigma*(n) the sum of unitary divisors d, meaning gcd(d,n/d)=1. Define s₀ and s₁ as sums of reciprocals of even and odd divisors, respectively. An ordinary perfect number P satisfies sigma(P)=2P; n is nonunitary perfect when sigma(n)-sigma*(n)=n.

We first classify the reciprocal equation. If n is odd then 2s₀-s₁<0. For n=2^a m with a>=1 and m odd, summing over the powers of 2 gives

    s₁=sigma(m)/m,  s₀=(1-2^(-a))sigma(m)/m,
    2s₀-s₁=(1-2^(1-a))sigma(m)/m.

For a=1 this is zero. For a>=2, put t=2^(a-1)-1; the equation 2s₀-s₁=1 is equivalent to

    t sigma(m)=(t+1)m.                                         (1)

When a=2, t=1 and (1) says m is an odd perfect number. When a>=3, t>=3 and coprimality of t and t+1 implies t divides m. Dividing (1) by tm gives sigma(m)/m=1+1/t. This ratio is the sum of reciprocal divisors of m and includes the distinct divisors 1 and t. Equality therefore excludes every other divisor; in particular m=t, and t is prime. Conversely, m=t prime satisfies (1).

The resulting n=2^(p+1)(2^p-1), p=a-1, are exactly four times the even perfect numbers by the classical Euclid–Euler theorem. Thus, without assuming whether odd perfect numbers exist, the solutions of 2s₀-s₁=1 are exactly four times all ordinary perfect numbers.

For a>=1, multiplicativity of sigma and sigma* yields

    sigma(n)-sigma*(n)
      =(2^a-2)sigma(m)+(2^a+1)(sigma(m)-sigma*(m))
      =n(2s₀-s₁)+(2^a+1)(sigma(m)-sigma*(m)).          (2)

The last difference is nonnegative and vanishes precisely when m is squarefree: unitary divisors are a subset of all divisors, and all divisors are unitary exactly for squarefree m. In particular, for an even nonunitary perfect n, 2s₀-s₁<=1, with equality exactly when m is squarefree.

Let L be Lagneau's conjectured equivalence, W the Ligh–Wall assertion that the nonunitary perfect numbers are exactly four times the even perfect numbers, and O the assertion that odd perfect numbers do not exist. We prove L iff W and O.

Assume L. If an odd perfect m existed, m could not be squarefree: if it has at least two distinct odd prime factors, sigma(m) is divisible by 4 whereas 2m is not; a single prime has sigma(m)=m+1<2m, and m=1 is not perfect. Thus sigma(m)-sigma*(m)>0. At n=4m the reciprocal equation holds, but (2) gives sigma(n)-sigma*(n)=n+5(sigma(m)-sigma*(m))>n, contradicting L. Hence O holds. The reciprocal classification and L now give W.

Conversely, if W and O hold, the reciprocal classification makes the reciprocal solutions exactly four times even perfect numbers, which W identifies with the nonunitary perfect numbers; hence L holds. Ligh and Wall already proved that every four times an even perfect number is nonunitary perfect; W asserts the matching converse as well. Neither W nor O is resolved here. The argument is human-checkable, not formally machine-checked.
