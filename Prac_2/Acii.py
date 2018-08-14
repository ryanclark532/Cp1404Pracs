def ver1():
    acii=input("Enter a character: ")
    while acii.isdigit():
        print("please enter a letter!")
        acii = input("Enter a character: ")
    print("The ACII code for {} is {}".format(acii,ord(acii)))
    upper=127
    lower=33
    number=int(input("enter a number: "))
    while number>upper or number<33:
            print("please enter a number between 33 and 127: ")
            number = input("enter a number: ")
    print("the character for {} is {}".format(number,chr(number)))
def ver2():
    ran=int(input("Hoq many colums do you want? max 127"))
    while ran>127:
        print("please enter a number smaller tha 127")
        ran = int(input("Hoq many colums do you want? max 127"))
    for i in range(33,ran):
        print("{} {:>2s}".format(i,chr(i)))
ver2()