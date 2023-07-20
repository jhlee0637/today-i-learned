[Python Program to Check Prime Number](https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/)
[에라토스테네스의 체 (소수구하기. 파이썬)](https://this-programmer.tistory.com/409)
[[Python] programmers, 프로그래머스 소수 찾기 Lv.1 (feat.에라토스테네스의 체)](https://aiday.tistory.com/68)
[[파이썬/python] 에라토스테네스의 체](https://ye333.tistory.com/24)
[Prime number](https://en.wikipedia.org/wiki/Prime_number)
[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
# Prime number
- A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.
- For example,
	- 2, 3, 5, ,7, 11, 13, 17, 19, ...

# Sieve of Eratosthenes
- Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers.
- The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant gap between them that is equal to that prime.
- To find all the prime numbers less than or equal to a given integer $\large n$ by Eratosthenes' method:
	1. Create a list of consecutive integers from 2 through $\large n$: 
	   (2, 3, 4, ..., $\large n$).
	2. Initially, let $\large p$ equal 2, the smallest prime number.
	3. Enumerate the multiples of $\large p$ by counting in increments of $\large p$ from 2$\large p$ to $\large n$,
	   and mark them in the list.
	   (these will be 2$\large p$, 3$\large p$, 4$\large p$, ...; the $\large p$ itself should not be marked)
	4. Find the smallest number in the list greater than $\large p$ that is not marked.
	   If there was no such number, stop.
	   Otherwise, let $\large p$ now equal this new number (which is the next prime),
	   and repeat from step 3.
	5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below $\large n$.
- Note that some of the numbers may be marked more than once
  (e.g., 15 will be marked both for 3 and 5).
  ## Python practice
```python
def prime_list(n):
    sieve = [True] * n #list of 'True'

    m = int(n ** 0.5) # numbers larger than the square root of 'n' will surely be removed by the sieve.
    for i in range(2, m + 1):
        if sieve[i] == True:           # if 'i' is prime 
            for j in range(i+i, n, i): # All multiples of 'i' are 'False'
                sieve[j] = False

    #return numbers based on the list of 'True'
    return [i for i in range(2, n) if sieve[i] == True]
```