import cs50
#inisialise the hight to a negative number
hight = -1

#loop to get a valid responce from the user
while hight < 1 or hight > 8:
    hight = cs50.get_int("Height:")
#draw the piramid by for loop
for i in range(1, hight + 1):
    print(" " * (hight - i) + "#" * i + "  " + "#" * i)