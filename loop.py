number=7

while True:
    user_input=input("Will you laike to play ? (y/n)")

    if user_input=='n':
        break

    user_number=int(input("Guess our number "))
    if user_number==number:
        print("You have gussed correctlt")
    elif abs(number-user_number) ==1:
        print("you are off by one number ")
    else:
        print("Sorry its wrong")

friends=["k","p","m","d"]

for i in friends:
    print(f"{i} is my friend ")
