print(input("Enter first name: "))
print(input("Enter last name: "))
print(input("Enter roll no.: "))

print('-' * 10)
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

print('-' * 10)
sum = (sub1 + sub2 + sub3 + sub4 + sub5)
percent = (sum / 500) * 100
if percent<= 100 and percent>= 75:
    print ("Grade A")
elif percent<= 74 and percent>= 60:
    print ("Grade B")
elif percent<= 59 and percent>= 40:
    print ("Grade C")
else:
    print("Fail")


