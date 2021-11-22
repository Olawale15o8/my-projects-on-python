# getting factorial of a specific number
studentinput = int(input("Enter your factorial number ! :"))
product = 1
numbers=[]
if studentinput < 0 :
      print("Check the number you enter")
for i in range(1,studentinput+1):
    product = product * i
    numbers.append(str(i))
numbers.reverse()
answer = "x".join(numbers)
print(f"the factorial of {studentinput}! = {answer} = {product}")
    		