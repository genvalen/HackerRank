#Original problem:
#https://www.hackerrank.com/challenges/py-if-else/problem

N = int(input())

if N%2 != 0 or(N%2==0 and N >= 6 and N <=20):
    print("Weird")
else:
    print("Not Weird")