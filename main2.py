import random
user_number = float(input("введіть своє число "))
if user_number < 1:
    user_number = float(input("введіть позитивне число "))
if user_number > 20:
    user_number = float(input("введіть своє число "))
number = random.randint(1, 20)
if user_number == number:
    print("ok")
NUMBER = number 
if user_number != NUMBER:
    while user_number != NUMBER:
        if user_number < 1:
            user_number = float(input("введіть позитивне число "))
        if user_number > NUMBER:
            print ("menshe")
            user_number = float(input("спробуйте ще раз "))
        else:
            print ("bolshe")
            user_number = float(input("спробуйте ще раз "))
        if user_number == NUMBER:
            print ("ok")
