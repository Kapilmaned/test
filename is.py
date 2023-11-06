number=7
user_input=input("Enter 'y' if you want to play >>>").lower()
if user_input == 'y':
    user_number=int(input("Guess our number "))
    if user_number==number:
        print("You have gussed correctlt")
    elif abs(number-user_number) ==1:
        print("you are off by one number ")
    else:
        print("Sorry its wrong")
        

