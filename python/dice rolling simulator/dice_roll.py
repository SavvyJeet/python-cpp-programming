#dice rolling simulator
import random
import time
message="This is the Dice Simulator Program..."
for i in message:
    print(i,end="")
    time.sleep(0.05)
print("\n----------------------------------------------\n")
while True:
    try:
        choice=input("Roll the Dice ? (yes/no): ")
    except ValueError:
        print("Please enter the correct input (yes or no)")
    if choice.lower()=="yes":
        print(f"You rolled {random.randint(1,6)}")
    elif choice.lower() == "no":
        print("thanks for playing")
        break
    else:
        print("Please enter yes or no")
