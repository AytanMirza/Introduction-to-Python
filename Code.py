#1. Take as input a person’s name and monthly salary in dollars, and print their yearly salary in
# thousands of dollars.For example: “Michelle”, “12345”  “Michelle’s yearly salary is $148K”.

def remove(string):
    return string.replace(" ", "")
name = input("Name: ")
salary = int(input("salary: "))
print(name + "'s", "yearly salary is", "${:,.0f}".format(round(((salary*12)/1000))), end=""'K')

#2. Take the following variables as real number inputs: A square’s side length; A circle’s radius
# Print “True” if the circle’s circumference is larger than the square’s, otherwise “False”.
square = int(input("Enter square length: "))
circle_radius = int(input("Enter circle radius: "))
print(2*3.14*circle_radius > 4 * square)

#3. Take as input a real number and print “True” if it’s in fact an integer, otherwise “False”.
a = float(input())
print(a == int(a))

#4. Take as input an integer number and print “True” if it’s an even number between 100 and 999, otherwise “False”.
a = int(input())
print(100 < a < 999 and a % 2 == 0)

#5. Take as input an integer number; assume the number is between 101 and 999, and that #its unit digit is not zero.
# Print the reversed number. For example: 256 -> 652.
n = int(input())
a = n % 10
b = (n // 10) % 10
c = (n // 100) % 10
print(str(a)+str(b)+str(c))

#6. Take as input two integers, and print: Their sum; Their difference; The product; The result of
# dividing the first by the second; The remainder when dividing the first by the second;“True” if
# the first number is bigger than or equal to the second otherwise “False”
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a >= b)






