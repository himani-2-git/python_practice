#Strings is a data type that stores a sequence of characters

str1 = "This is a first string"
str2 = 'strings can be written in single quotes too'
str3 = """this is a string written in tripple quote"""

str4 = "This is himani's vs code"

#escape sequence characters 
#\n for next line, \t for tab gap

str5 = "hello, i am himani. \ni am 21 years old."
print(str5)

str6 = "helloworld \thimani here"
print(str6)

#operations on strings
#concatenation 
str7 = "hello"
str8 = "world"
print(str7 + str8)

str9 = "ice"
str10 = "cream"
final_str = str9 + str10
print(final_str)

str11 = "raw"
str12 ="mango"
final_str1 = str11 + " " + str12
print(final_str1)

#length of string

#len(str) is a function which counts lenth of string
str_1 = "homosapien"
print(len(str_1))

print(len(final_str1))
#length calculate letters, digits, spaces, symbols, everything mentioned in the string.

#Indexing in strings
#It is nothing but numbering of characters inside strings, in python indexing starts from 0,1,2 and so on.

str_2 = "Himani"
ch = str_2[0]
print(ch)

print(str_2[1])
print(str9[0])

#we can acess the character but we cannot modify them in indexing.

#Slicing of a string
#Accessing a part of a string str starting_index : ending_index
# Include the starting index, but exclude the ending index.

str13 = "Strawberry Cake"
print(len(str13))
print(str13[5 : 12]) 
print(str13[0 : 4])
print(str13[5 : 9])
print(str13[12 : 15])
print(str13[11 : len(str13)])
print(str13[0 : 5])
print(str13[5 : 10])
#don't always need to write the start or end index
print(str13[:5])   # Straw
print(str13[5:])   # berry Cake
print(str13[:])    # Strawberry Cake  



#negative index slicing 
#starts from the last letter of the word counting down towards the left

str14 = "Apple"
print(str14[-3 : -1])

#string functions

str15 = "i am studying engineering"
print(str15.endswith("ng")) #returns true if the word ends with the "ng" or false
print(str15.capitalize()) #capitalize 1st letter in new string, works 1 time only
print(str15.replace("studying", "learning")) #(old, new) replaces all occurences of old string values
print(str15.find("n")) #returns 1st index of the 1st occurrer
print(str15.find("z")) #returns in minus if the letter does not exist
print(str15.count("am")) #count the occrrence of substr



#write a program to input user's first name and print it's length

a = input("Enter your first name: ")
print("length: ", len(a))

#write a program to find occurence of '$' in a string

string1 = "Dev buys a share of $1,00,000 in a share market. The share falls over $4,00,000 down and rises up $6,00,000 more in the morning, making profit of $2,00,000."
print(string1.count("$"))

#nesting

age_2 = int(input("Enter your age: "))
if(age_2 >=  18):
    if(age_2 >=58):
        print("Cannot join the company")
    else:
        print("Can join the company")
else:
    print("not applicable")


#question 1

#write a program if a number entered by the user is odd or even

#if the number is divided by 2 and gives reminder 0, its even else it's odd

num = int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

#write a code to find greatest of 3 numbers entered by the user

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x >=y and x >=z:
    print("greatest: ", x)
elif y>=x and y>=z:
    print("greatest: ", y)
else:
    print("greatest: ", z)

#write to check if a number is a multiple of 7 or not

num_2 = int(input("Enter a number: "))
if num%7==0 :
    print("Multiple of 7")
else:
    print("Not a multiple of 7")

