# Collatz Conjecture Testing
Read as 'code'

This code was requested informally on a MAC0110 class lessoned by Roberto Hirata, 1st semester of 2024. I did not code it when requested, but decided to do it on the recess.
Initially, it only received a natural number N and printed all resulting numbers (because it looks cool on Python's IDLE), counting what we will call  here "interactions".
A statistics undergraduate friend of mine, Eduardo Yukio, asked me to graph the results of the number of interactions from 1 to N, so I did it. Also, I altered the initial code to graph the result of every interaction using pyplot.

On Collatz's Conjecture, it states that every natural number (0 not included), having a specific function applied to it and its results will converge to 1. The function can be write as:
def f(x):
    if x % 2 == 0:
        return x/2
    else:
        return 3 * x + 1

That is, if a number is even, it resturns its half and, if odd, returns the tripple of the number and sums 1.
