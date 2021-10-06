#coding=gbk
'''Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?、
result：6857
最大公约数的算法：从2开始不断累加去除此数，如果能整除就让这个数设置为除数。最后那个能整除的书就是最大质因数。
就像例子上的数字 ： 13195 = 5 x 7 x 13 x 29
'''
d, n = 2, 600851475143
while (d  < n):
  if n % d == 0:
    n /= d
  else: d += 1
print n