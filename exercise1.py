N = int(input("enter a number: "))
#check for every number from 1 to N
for i in range(1,N+1):
  #check if current number is prime
  if(isPrime(i)):
    print(i,end=" ")
