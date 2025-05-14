
#1- Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

firstname = input("enter your first name :")
lastname = input("enter your lastname : ")

firstnamerev = firstname[::-1]
lastnamerev  = lastname[::-1]

print (firstnamerev,"", lastname )


# 2- Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5

n = int(input("Enter an integer: "))

ans= n + int(str(n)+str(n))+int(str(n)*3)

print(f"The result is: {ans}")

#3- Write a Python program to print the following here document.
#Sample string :
#a string that you "don't" have to escape
#This
#is a ....... multi-line
#heredoc string --------> example

print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')

#4- Write a Python program to get the volume of a sphere with radius 6.


pi = 3.14
r = int(input("enter thr raduis :"))
vol= (4/3)*pi*r**3
print(f"The volume of the sphere with radius {r} is: {vol:.2f}")






#5- Write a Python program that will accept the base and height of a triangle and compute the area.

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print(f"The area of the triangle is: {area:.2f}")



#6- Write a Python program to construct the following pattern, using a nested for loop.
#Search about method
#end=””


rows = 6


for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")  # Print '*' on the same line
    print()  # Move to the next line after each row


for i in range(rows - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")  
    print()  



#7- Write a Python program that accepts a word from the user and reverse it.


word = input("Enter a word: ")
reve = word[::-1]
print(f"The reversed word is: {reve}")



#8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for number in range(7):
    if number != 3 and number != 6:
        print(number, end=" ")



#9-Write a Python program to get the Fibonacci series between 0 to 50
#Note : The Fibonacci Sequence is the series of numbers :
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34


def fibonacci():
    a, b = 0, 1
    while a <= 50:
        if a > 0:  
            print(a, end=" ")
        a, b = b, a + b  


fibonacci()

#10


input_string = input("Enter a string: ")


digits = 0
letters = 0


for char in input_string:
    if char.isdigit():  
        digits += 1
    elif char.isalpha():  
        letters += 1


print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")






