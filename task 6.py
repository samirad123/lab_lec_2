# Python Program to check character is Alphabet Digit or Special Character
ch = input("Please enter a character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("This character ", ch, "is an alphabet")
elif(ch >= '0' and ch <= '9'):
    print("This character ", ch, "is a digit")
else:
    print("This character ", ch, "is a special character")

