print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if (x + y) > z or (y + z) > x or (x + z) > y:
    print("It is a triangle")
else:
	print("It is not a triangle")

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")

