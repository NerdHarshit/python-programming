#program to convert myclass.roman numbers to int and vice versa

class myclass:
    roman = ""

num = input("enter your number in int")#take str


def digit4(x):
    match x:
        case "1":
            myclass.roman = myclass.roman + "M"
        
        case "2":
            myclass.roman = myclass.roman + "MM"

        case "3":
            myclass.roman = myclass.roman + "MMM"

        case _:
            myclass.roman  = myclass.roman + "."
            

def digit3(x):
    match x:
        case "0":
            myclass.roman = myclass.roman + ""

        case "1":
            myclass.roman = myclass.roman + "C"
        
        case "2":
            myclass.roman = myclass.roman + "CC"

        case "3":
            myclass.roman = myclass.roman + "CCC"

        case "4":
            myclass.roman = myclass.roman + "CD"

        case "5":
            myclass.roman = myclass.roman + "D"

        case "6":
            myclass.roman = myclass.roman + "DC"

        case "7":
            myclass.roman = myclass.roman + "DCC"

        case "8":
            myclass.roman = myclass.roman + "DCCC"

        case "9":
            myclass.roman = myclass.roman + "CM"
        
        case _:
            myclass.roman  = myclass.roman + "."


def digit2(x):
    match x:
        case "0":
            myclass.roman = myclass.roman + ""

        case "1":
            myclass.roman = myclass.roman + "X"
        
        case "2":
            myclass.roman = myclass.roman + "XX"

        case "3":
            myclass.roman = myclass.roman + "XXX"

        case "4":
            myclass.roman = myclass.roman + "XL"

        case "5":
            myclass.roman = myclass.roman + "L"

        case "6":
            myclass.roman = myclass.roman + "LX"

        case "7":
            myclass.roman = myclass.roman + "LXX"

        case "8":
            myclass.roman = myclass.roman + "LXXX"

        case "9":
            myclass.roman = myclass.roman + "XC"
        
        case _:
            myclass.roman  = myclass.roman + "."


def digit1(x):
    match x:
        case "0":
            myclass.roman = myclass.roman + ""

        case "1":
            myclass.roman = myclass.roman + "I"
        
        case "2":
            myclass.roman = myclass.roman + "II"

        case "3":
            myclass.roman = myclass.roman + "III"

        case "4":
            myclass.roman = myclass.roman + "IV"

        case "5":
            myclass.roman = myclass.roman + "V"

        case "6":
            myclass.roman = myclass.roman + "VI"

        case "7":
            myclass.roman = myclass.roman + "VII"

        case "8":
            myclass.roman = myclass.roman + "VIII"

        case "9":
            myclass.roman = myclass.roman + "IX"
        
        case _:
            myclass.roman  = myclass.roman + "."

# all fx ends here
d = len(num)

for i in range(d,0,-1):
    match i:
        case 4:
            digit4(num[d-i])
        
        case 3:
            digit3(num[d-i])

        case 2:
            digit2(num[d-i])

        case 1:
            digit1(num[d-i])

        case _:
            print("error")


print()
print(myclass.roman)

