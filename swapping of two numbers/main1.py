try:
  a = int(input("Enter the value of a : "))
  b = int(input("Enter the value of b : "))
  if a==b:
    print("both are same numbers!")
  else:
    print(f"currently a = {a}\nb = {b}")
    a,b = b,a
    print(f"After swapping: a = {a}, b = {b}")
except ValueError:
  print("Enter valid integer !")
