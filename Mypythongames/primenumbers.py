# prime numbers
def primenumbers() :
  notprime =[] 
  prime = []
  b=int(input('Enter the range of the number u want to check for its prime numbers'))  
  for a in range(1, b):
     if (a > 1):
         for i in range(2,a) :
            if (a % i)== 0 :
                notprime.append(a)
                break 
            prime.append(a) 
  result=set(prime)
  print(f"{result}" )
primenumbers()           

 
          
           

           

 
     