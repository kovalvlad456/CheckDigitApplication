basicCode = []
upcCode = []
positionCode = []
noneCode = []

def basic (userCode): # function for basic code
    sum = 0
    checkDigit = 0
    lastChar = userCode[-1:]
    for i in userCode[:-1]: #for looping usercode
        sum += int(i) #adding value of i to the sum
        checkDigit = sum % 10 # getting the remainder of 10 from the sum
    if int(lastChar) == int(checkDigit): #if last digit equals remainder
        basicCode.append(userCode) #add to basic code list
        print("code:", userCode, "valid basic ") # output valid
    
def positional (userCode): #function for position
    lastCharPos = userCode[-1:]
    positionalSum = 0
    positionalRem = 0
    for x in range (0, len(userCode[:-1])): # for looping the usercode
        position = int(userCode[x]) * int((x+1)) # x multiplied by the element by x
        x += 1 #adding 1 to x
        positionalSum += position
        positionalRem = positionalSum % 10 # getting the remainder for 10
    if int(lastCharPos) == int(positionalRem):
        positionCode.append(userCode) # adding to the position code list
        print("code:", userCode, "valid positional")



def upc (userCode):#function for upc code
    upcSum = 0
    lastCharUpc = userCode[-1:]
    for z in range(len(userCode[:-1])): #for looping the usercode
        if int(z+1) % 2 == 0: #if number is even
            upcSum += int(userCode[z]) * 1   #multiply element by 1
        else:
            upcSum += int(userCode[z]) * 3#multiply element by 3
    upcRem = upcSum % 10#getting the remainder of 10
    if upcRem > 0:
        upcRem = 10 - upcRem
    if int(lastCharUpc) == int(upcRem):
        upcCode.append(userCode)
        print("code:", userCode, "valid UPC")
    if userCode not in basicCode and userCode not in positionCode and userCode not in upcCode: # if usercode is in none of the lists
        noneCode.append(userCode) #add to the none list
        print("Code: ", userCode, "not basic, positional, or upc")# print statement





