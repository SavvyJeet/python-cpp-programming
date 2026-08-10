print("This programme is to find the arithmetical operations on two numbers")
try:
  num1=int(input("Please enter the first value: "))
  num2=int(input("Please enter the second value: "))
except ValueError:
  print("please provide only the numbers as input !")
else:
  print("Press 1 to get their sum\nPress 2 to get their difference\nPress 3 to get their product\nPress 4 to get their divsion\nOR Press 5 to get all these at once")
  try:
    press=int(input("Provide your choice: "))
    print("-"*25)
  except ValueError:
    print("please provide correct choice as input !")
  else:
    if press==1:
      print("the sum of",num1,"and",num2,"is",num1+num2)
    elif press==2:
      print("the difference of",num1,"and",num2,"is",num1-num2)
    elif press==3:
      print("the product of",num1,"and",num2,"is",num1*num2)
    elif press==4:
      try:
        print("the division of",num1,"and",num2,"is",num1/num2)
      except ZeroDivisionError:
        print("Here Division by 0 Not Defined : Cannot divide by zero")
    elif press==5:
      print("OK")
      print("the sum of",num1,"and",num2,"is",num1+num2)
      print("the difference of",num1,"and",num2,"is",num1-num2)
      print("the product of",num1,"and",num2,"is",num1*num2)
      try:
        print("the division of",num1,"and",num2,"is",num1/num2)
      except ZeroDivisionError:
        print("Here Division by 0 Not Defined : Cannot divide by zero")
    else:
      print("Invalid Choice! Please enter a number from 1 to 5.")
