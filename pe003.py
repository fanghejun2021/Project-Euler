#coding=gbk
'''Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?��
result��6857
���Լ�����㷨����2��ʼ�����ۼ�ȥ������������������������������Ϊ����������Ǹ�������������������������
���������ϵ����� �� 13195 = 5 x 7 x 13 x 29
'''
d, n = 2, 600851475143
while (d  < n):
  if n % d == 0:
    n /= d
  else: d += 1
print n