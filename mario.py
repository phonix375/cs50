import cs50
hight = -1
while hight < 1 or hight > 8:
    hight = cs50.get_int("Height:")
for i in range(1,hight+1):
    print(" " * (hight - i) +"#"*i+"  "+ "#" * i)