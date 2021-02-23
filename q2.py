import math

def isPrime(number):
    if(number<=1):
        return False;
    elif(number ==2):
        return True
    sqr = int(number**(1/2))+1
    pme = [True]*sqr
    for i in range(2,sqr,1):
        if(pme[i]):
            if(number % i==0):
                return False
            for j in range(i+i,sqr,i):
                if(j%i==0):
                    pme[j] = False
    return True

def floating_prime(number):

    for i in range(4):
        if(isPrime(int(number))):
            return True
        number=number*10
    return False
        
# while(True):
#     number=input()
#     if(number=="0.0"):
#         break
#     print(floating_prime(number))

    
x = float('1.657')
print(floating_prime(x))