def sieve(n):
    primes=[0]*(n+1)
    primes[0],primes[1]=1,1
    for i in range(2,n+1):
        if primes[i]==0 and i*i<n:
            for j in range(i*i,n+1,i):
                primes[j]=1
                
    for t in range(1,n+1):
        if primes[t]==0:
            print(t)
sieve(100)