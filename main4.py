password = 1234
user_password = float(input("введіть свій пароль "))
if user_password == password:
    print("ok")
if user_password != password:
    while user_password != password:
        if password != user_password:
            print ("пароль не вірний")
            user_password = float(input("введіть свій пароль "))
print ("пароль вірний ")