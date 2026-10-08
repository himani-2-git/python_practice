print("hello world!")
print("Himani is learning python programming")

print("Python is a high level language", "Developed by Guido van Rossum", "in 1991")
print("python is a case sensitive language")

print(21)
print(20+1)

print("Variables : A name given to a memory location that stores data values")
name = "Himani"
age = 21
price = 25.99
rate = '24k'
print(name, age, price, rate)

print("Strings are written in single/ double quotes")

print("My name is", name)
print("My age is", age)

age_2 = -21

print("Variables can be combination of upper, lower cases, digits, underscore")
print("variable1 is valid, but 1variable is invalid")
print("symbols like @, $, %, #, etc are not allowed in variable names")
print("variables should be simple short and meaningful")


print("Data types")
print("There are various data types in python : integers, strings, float, boolean, none")
print("These are also called as primitive/ primary data types")

print("integers are whole numbers")
print(type(age))
print(type(age_2))

print("strings are sequence of characters")
name = "himani"
name_2 = 'antara'
name_3 = '''varsha'''

print(type(name))
print(type(name_2))
print(type(name_3))

print("float are decimal numbers")
price = 34.99
print(type(price))
print("The price of my shoes is $", price)

print("boolean have only two values : True / False")
print("T of True and F of false should be capital, else it will be considered as a string")
rate = 100
value = True
a = None
print("1kg apples are for Rs.", rate, value)

print(type(value))
print(type(a))


print("Keywords")
print("keywords are reserved words in python that have special meanings")
print("they cannot be used as variable names")
print("examples of keywords: if, else, for, while, def, class, import, etc.")

print("comments in python")
#This is a comment


print("Arithmetic operations")
print("used to perform mathematical operations")

a = 2
b = 3
total = a+b
diff = a-b
prod = a*b
quo = a/b
mod = a%b    #reminder
power = a**b   #a^b

print(total)
print(diff)
print(prod)
print(quo)
print(mod)
print(power)


print("Comparison operators")
print("Comparison operators are used to compare values")

a = 40
b = 90

print(a==b) #equal to
print(a!=b) #not equal to
print(a>b)  #greater than
print(a<b)  #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to


print("Assignment operators")
print("used to assign values to variables")

p = 15
p = p + 5 #15 + 5 = 20
print(p)

q = 20
q += 5 #also means q = q + 5
print(q)

num = 10
num += 4 # 10 + 4 = 14
print(num)

num -= 4 # 14 - 4 = 10
print(num)

num /= 4 # 10 / 4 = 2.5
print(num)

num *= 4 #2.5 * 4 = 10.0
print(num)

num %= 4 # 10.0 % 4 = 2.0
print(num)

num **= 4 # 2.0 ^ 4 = 16.0
print(num)


print("Logical operators")
print("are used to combine conditional statements, works on boolean values")
print("and : returns True if both statements are True")
print("or : returns True if one of the statements is True")
print("not : returns True if the statement is false")

mina = 30
tina = 24
print(not False) #not of False is True
print("not operator :", not (tina > mina)) #gives True because tina is not greater than mina

print("and operator : ", mina > tina and tina < mina) #gives True because both statements are true
print("and operator : ", mina > tina and mina < tina) #gives False because mina is not less than tina 
#in both statements should be true for and operator to return True

print("or operator : ", mina > tina or mina < tina) #gives True because one of the statements is true
#in or operator if one of the statements is true, it will return True


value1 = True
value2 = False
print("AND :", value1 and value2)
print("OR :", value1 or value2)
print("NOT :", not value1)
print("NOT :", not value2)

a1 = 50
a2 = 30
print("Result:", a1==a2 or a1>a2)
print("Result:", a1==a2 or a1<a2)
print("Result:", a1!=a2 or a1>a2)


print("Type conversion")

x = 4
y = 3.58
total = x + y
print(sum)
print(type(x))
print(type(y))
print(type(sum))


print("Type conversion is used to convert one data type into another data type")


print("Type casting")

i = "20" #string
g = int("20") #string to integer
h = 7
print(g + h)
print(type(i))
print(type(g))
print(type(h))

pi = 3.14
pi = str(pi) #float to string
print(type(pi))


print("Input in python")

print("input() is used to accept values from user, it always returns string value")
input("Enter your name : ")

age = input("Enter your age : ")
print("Your age is", age)

val = input("Enter a value : ")
print(type(val), val)
#input() → always str → use int() / float() if you need a number

age = int(input("Enter your age : "))
print("Your age is", age)

val = float(input("Enter a value : "))
print(type(val), val)


first = int(input("Enter First value : "))
second = int(input("Enter Second value : "))
print("Sum = ", first + second)


side = float(input("Enter side of square :"))
print("Area of the square : ", side * side) # OR side ** 2


u = float(input("Enter First value : "))
v = float(input("Enter Second value : "))
print("avg =", (u+v)/2)

m = int(input("Enter First value : "))
n = int(input("Enter Second value : "))
print(m >= n)

