import cs50


# this is the first comment
def checkVlid(number):
    x = ''
    number = number[::-1]
    for i in range(1, len(number), 2):
        x = x + str(int(number[i])*2)
    x = [int(d) for d in x]
    Sum = sum(x)
    x = ''
    for i in range(0, len(number), 2):
        x = x + str(int(number[i]))
    x = [int(d) for d in x]
    Sum += sum(x)
    # this is the good
    if Sum % 10 == 0:
        return True
    # this is the not so good!
    else:
        return False


# this is the second comment
number = cs50.get_string("Number: ")
if len(number) in [15, 16, 13]:
    odd = 0
    even = 0
    # WOOW this is another comment

    for i in range(0, len(number), 2):
        odd += int(number[i])
    for i in range(1, len(number), 2):
        even += int(number[i])
    # ok this will be the last one
    if number[0]+number[1] in ["34", "37"]:
        if checkVlid(number):
            print("AMEX")
        else:
            print("INVALID")
    elif number[0]+number[1] in ["51", "52", "53", "54", "55"]:
        if checkVlid(number):
            print("MASTERCARD")
        else:
            print("INVALID")
    elif number[0] == "4":
        if checkVlid(number):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")
# ooo no this is the last comment