# Multiples of 3 or 5

## Problem
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Follow up
* Implement solution where user can pass any limit number (not only 1000).
* Implement solution where user can pass any number of dividers.

## Solution
### Naive solution
Go in a loop and check the condition for every potential multiple.
```
sum_of_multiples = 0
FOR potential_multiple in {2 .. 1000}:
    IF potential multiple is divided by at least one divider:
        sum_of_multiples += potential_multiple
    END
END
PRINT(sum_of_multiples)
```

Memory complexity: `O(1)`.

Time complexity: `O(N)`, where N is a maximum value of potential multiple.

### Improved solution
In case there is only two dividers it's possible to prepare a specific math formula.

Let's try to calculate the sum of all multiples for the single divider. There are numbers `{1 .. N}` and divider `X`. Then multiples are: `{X, X+1X, X+2X, ..., X+mX} | X+mX < N/X`. Also it can be presented as `X * (1 + 2 + 3 + ... + N/X)`

Hence we have a typical arithmetic progression.

So **sum of multiples for a single divider** is: `X * (N/X * (N/X+1) / 2) = N * (N/X+1) / 2`.

Now it's possible to calculate separately sum for divider 3 and 5. But there are numbers calculated twice: 15, 30, 45, ... . It's necessary to subtract these numbers. Actually all such numbers will be multiples of [LCM](https://en.wikipedia.org/wiki/Least_common_multiple)(3, 5).

That is why the final formula is:
`sum_of_multiples(3) + sum_of_multiples(5) - sum_of_multiples(lcm(3, 5))`.

Memory complexity: `O(1)`

CPU complexity: `O(1)`
