print("This programme is to find the arithmetical operations on two numbers")
num1=int(input("Please enter the first value: "))
num2=int(input("Please enter the first value: "))
print("Press 1 to get their sum\nPress 2 to get their difference\nPress 3 to get their product\nPress 4 to get their divsion\nOR Press 5 to get all these at once")
press=int(input("Provide your choice: "))
print("-"*25)
if press==1:
  print("the sum of",num1,"and",num2,"is",num1+num2)
elif press==2:
  print("the difference of",num1,"and",num2,"is",num1-num2)
elif press==3:
  print("the product of",num1,"and",num2,"is",num1*num2)
elif press==4:
  print("the division of",num1,"and",num2,"is",num1/num2)
elif press==5:
  print("OK")
  print("the sum of",num1,"and",num2,"is",num1+num2)
  print("the difference of",num1,"and",num2,"is",num1-num2)
  print("the product of",num1,"and",num2,"is",num1*num2)
  print("the division of",num1,"and",num2,"is",num1/num2)
else:
  print("No input Given")
