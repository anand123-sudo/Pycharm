
#
# print("1 for addition")
# print("2 for subtraction")
# print("3 for multipication")
# print("4 for devide")
#
# #print("If you add type 1, sub type 2 , mul3")
# a=int(input("Enter the chose:-"))
#
# x=int(input("Enter the No:-"))
# y=int(input("Enter the No."))
#
# if a==1:
#     print(x+y)
# elif a==2:
#     print(x-y)
# elif a==3:
#     print(x*y)
# else:
#     print("select valid No.")

def calculator(choise,x,y):
    if choise==1:
        return x+y

    elif choise==2:
        return x-y

    elif choise==3:
        return x*y

    elif choise==4:
        return x/y

    else:
        return "invalid number"