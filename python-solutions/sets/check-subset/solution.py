# Original problem: https://www.hackerrank.com/challenges/py-check-subset/problem
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, s1 = int(input()), set(input().split())
        b, s2 = int(input()), set(input().split())
        print(s1.issubset(s2))
        