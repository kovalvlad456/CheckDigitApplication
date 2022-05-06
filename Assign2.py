from code_check import *
counter = 1

while counter != 0: #counter does not equal to zero
    userCode = str(input("Please enter code (digits only) (enter 0 to quit) ")) #get the usercode
    if userCode == "0":#if usercode equals zero stop the loop
        counter - 1
        break
    basic(userCode) #calling all three function from code_check
    positional(userCode)
    upc(userCode)

#if lists are empty append none to them
if not upcCode:
    upcCode.append("none")
if not positionCode:
    positionCode.append("none")
if not basicCode:
    basicCode.append("none")
if not noneCode:
    noneCode.append("none")

separator = ", "
print("Summary " +"\n" + "Basic: ", separator.join(basicCode), "\n" + "Position: ", separator.join(positionCode), "\n" + "UPC: ", separator.join(upcCode), "\n" + "None: ", separator.join(noneCode))      
#printing the final statement when user enters 0

        



