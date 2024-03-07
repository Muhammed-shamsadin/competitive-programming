'''
1. we check if the number after our input n is a prime or not
2. if it is not a prime it will increase by 1, but if it is a prime
3. We will print "YES" for the next prime (m) after n 
4. print "NO" if it is not the next prime(m) or if it is not a prime number at all.
'''
n, m = [int(i) for i in input().split()]

a = n + 1

while True:
    prime = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            prime = False
            break
    if prime:
        break
    a += 1

if a == m:
    print("YES")
else:
    print("NO")


