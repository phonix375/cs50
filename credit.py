import cs50

def checkVlid(number):
    x = ''
    number  = number[::-1]
    for i in range(1, len(number), 2):
        x = x + str(int(number[i])*2)
    x = [int(d) for d in x]
    Sum = sum(x)
    x = ''
    for i in range(0, len(number), 2):
        x = x + str(int(number[i]))
    x = [int(d) for d in x]
    Sum += sum(x)
    if Sum % 10 == 0:
        return True
    else: return False

number = cs50.get_string("Number: ")
if len(number) in [15,16,13]:
    odd = 0
    even = 0
    for i in range(0, len(number), 2):
        odd += int(number[i])
    for i in range(1, len(number), 2):
        even += int(number[i])

    if number[0]+number[1] in ["34","37"]:
        checkVlid(number)
        print("AMEX")
    elif  number[0]+number[1] in [ "51", "52", "53", "54", "55"]:
        checkVlid(number)
        print("MASTERCARD")
    elif number[0] == "4":
        checkVlid(number)
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
