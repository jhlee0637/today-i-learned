[[Python] 최소공배수, 최대공약수란? 파이썬 알고리즘으로 쉽게 구현하기](https://codingpractices.tistory.com/34)
[Greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor)
[Least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple)
[Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
# Greatest Common Divisor(GCD), 최대공약수
## What is GCD
- In mathematics, the greatest common divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. 
	- Divisors of 8
		- 1, 2, 4, 8
	- Divisors of 10
		- 1, 2, 5, 10
	- Common divisors of 8 and 10
		- 1, 2
	- Greatest Common Divisor
		- 2
## What is the feature of GCD
- When you divide two numbers by their GCD, there is no remainder.
## Python practice
```python
A = 8
B = 10

for number in range(1, min(A, B)):
	if number!=1 and A%number == 0 and B%number == 0:
		print(number)
		break
```
# Least Common Multiple(LCM), 최소공배수
## What is LCM
- In arithmetic and number theory, the least common multiple, lowest common multiple, or smallest common multiple of two integers $\huge a$ and $\huge b$, usually denoted by $\huge lcm(a, b)$, is the smallest positive integer that is divisible by both $\huge a$ and $\huge b$.
	- Multiples of 4
		- 4 , 8 , 12 , 16 , 20 , 24 , 28, 32, 36, 40, 44, 48, ...
	- Multiples of 6
		- 6 , 12 , 18 , 24 , 30 , 36 , 42, 48, ...
	- Common multiples of 4 and 6 are the numbers that are in both lists
		- 12, 24, 36, 48, 60, 72, ...
	- Least Common Multiple
		- 12
## What is the feature of LCM
- When LCM is divided by two numbers, there is no remainder.
- LCM can be computed from the GCD with the formula, $$\Huge lcm(a,b) = \frac{|ab|}{gcd(a,b)}$$
## Python practice
```python
A = 4
B = 6

for number in range(max(A, B), (A*B)+1):
	if number%A == 0 and number%B ==0:
		print(number)
		break
```
# Euclidean Algorithm, 유클리드 호제법

- In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two integers (numbers), the largest number that divides them both without a remainder.
	- Remainder of 10/12 = 10
	- Remainder of 12/10 = 2
	- Remainder of 10/2 = 0
		- 2 is the GCD of 10, 12

|10|%|12|=|10|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| | |12|%|10|=|2|
| | |  | |10|%|2|=|0|

## Python practice
```python
A = 10
B = 12

while(B):
	A, B = B, A%B

print ("GCD:", A)
```

- To get LCD with Euclidean Algorithm, using the feature of LCD with the formula, $\Huge lcm(a,b) = \frac{|ab|}{gcd(a,b)}$
```python
#GCD
A = 10
B = 12

while(B):
	A, B = B, A%B

GCD=A


#LCM
A = 10
B = 12

LCM=(A*B)//GCD

print("LCM:", LCM)
```