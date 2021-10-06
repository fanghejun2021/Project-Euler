#coding=gbk
'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
本质上是求1到20的最大公约数。 1 x 2 x 3 x 2(4) x 5 x 7 x 2(8) x 3(9) x 11
x 13 x 2(16) x 17 x 19

如果用程序来算呢？
'''
print 1*2*3*2*5*7*2*3*11*13*2*17*19