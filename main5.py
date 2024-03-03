user = input("введіть ваше речення ")
new_user = ""

for i in user:
    if i.islower():
        new_user += i.upper()
    else:
        new_user += i.lower()

print(new_user)
