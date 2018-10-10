#__author:iruyi
#date:2018/9/13

_user = "lys"
_pwd = "abc"

# for i in range(3):
#     username = input("name:")
#     password = input("password:")
#     if(_user == username and _pwd == password):
#         print("Welcome to python....")
#         break;
#     else:
#         print("Name or password is wrong")
# else:
#     print("You have input 3 times wrong name or password")

i = 1
while i<=3:
    username = input("name:")
    password = input("password:")
    if (_user == username and _pwd == password):
        print("Welcome to python....")
        break;
    else:
        print("Name or password is wrong")

    i += 1

    if i == 4:
        ask = input("Do you want to try again ? Y or N")
        if ask == "Y":
            i = 1

else:
    print("You have input 3 times wrong name or password")


