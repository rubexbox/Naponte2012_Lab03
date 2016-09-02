# COT 4930  Python Programming
# name: Nicolas Aponte
# id  : Z23216341
# lab : 03
# Program which simulates the Sieve of Eratothenes
def eratos(n):
    sieve=[2]
    for n in range (2, length):
        sieve.insert(n-1, n+1)
        
    
    for m in range (0, len(sieve)):
        if(m!=len(sieve)):
            for h in range (m+1, len(sieve)):
                if (h<len(sieve)):
                        if (sieve[h]%sieve[m]==0):
                            sieve.remove(sieve[h])
                
    print_primes(sieve)

def print_primes(primes):
    v=0
    for j in range (0, len(primes)):
        if (v==9):
            print (primes[j])
            v=0
        else:
            print ("%-5d"% primes[j],end='')
            v+=1


length=eval (input("To what number do you want to go to? "))
if ((length<2)|(length>300)):
    print("ERROR: Upper Bound out of range.")

else:
   eratos(length)
        
   
