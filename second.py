# a = 4
# print(type(a))
# b = 3.5
# print(type(b))
#
# c = 'salam'
# print(type(c)) # float

# my_var2 = 'salam'

# my_word = "Yasin"
# my_word_2 = 'Yasin'

"""
SECOND LESSON
"""
# Casting
# x = 5.8 # float
#
# y = int(x)
# print(y)


# x = 5 # integer
# y = str(x)  # "5"

# a = "3"
# b = float(a)
# print(b)

# a = "A3"
# b = float(a)
# print(b)

# Strings

# my_string = """
# salam
# necesen
# salam
# """
# print(my_string)

# my_string = "Hello World!"
# print(my_string[0:5:2])


# my_word = "Yasin"
# print(len(my_word))  # length = uzunluq

# my_word = input("Enter your name: ")
# print(my_word)

# my_age = int(input("Enter your age: ")) # "23"
# print(my_age + 3) # 26
# print(my_age + 2) # 25


# my_number = 3
# # my_number = my_number + 2 # 5
# # my_number = my_number * 3 # 15
# my_number += 2 # my_number = my_number + 2

# print(my_number)


# my_word = "intigam"
#
# new_word = my_word.upper() # lower
#
# print(new_word)

# name
# surname

# Intigam Guluzade

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
#
# full_name = name + " " + surname

# print(full_name)

# age = 17
# # my_text = "Yasin is " + age # Yasin is 17
# my_text = f"Yasin is {age}"
# print(my_text)

# my_text = 'Menim en sevdiyim serial "Sherlock Holmes"'
# print(my_text)

# name = "intigam"
# name = name.capitalize()
# print(name)
"""
1. Istifadeciden 2 eded alin ve onlarin cemini bir deyisene menimesederek ekrana cap edin.
2. Daxil olunan sozde ilk 3 herfi cap eden python kodu yazin.
3. Daxil edilen 2 ededin ferqlerinin, cemlerinden ne qeder boyuk oldugunu tapan python kodu yazin.
4. Istifadeciden bir soz alin ve onun uzunlugunu ekrana cap edin.
5. Daxil edilen sozun son herfini cap eden python kodu yazin.
6. Daxil edilen ededin reqemlerinin sayini tapan python kodu yazin.
7. Daxil edilen ikireqemli ededin reqemleri cemini tapan python kodu yazin.
8. Daxil edilen sozde tek yerde duran herfleri cap eden python kodu yazin.
9. Daxil edilen sozde cut yerde duran herfleri cap eden python kodu yazin.
10. Daxil edilen sozun ilk 3 herfi ile son herfini birlesdirib, yeni bir deyisene menimsedib, ekrana cap edin.
11. Uzunlugu tek sayda olan, daxil edilen sozun ortada duran herfini ekrana cap edin.
12. Istifadecinin daxil etdiyi 3 ededin ededi ortasini tapan program
"""

# 1.
# a = int(input("Enter the first element: ")) # 32
# b = int(input("Enter the second element: ")) # 24
#
# c = a + b # 3224, 56
# print(c)

# 2.
# a = input("Enter word: ")
# # print(a[:3])
# print(a[3:])

"""
32, 24, 56

(32+24+56)/3

"""

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = a - b
# d = a + b
#
# print(d - c)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print((a + b + c)/3)

# a = input("Enter the word: ")
# print(len(a))


# a = input("Enter the word: ")
# print(a[len(a) - 1])  # a[4]

# a = input("Enter the number: ")
# print(len(a))


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(a + b)

# a = 48 , 4 ve 8

#7.
# number = input("Enter the 2 digit number: ") # 45
#
# first_digit = int(number[0]) # 4
# second_digit = int(number[1]) # 5
#
# print(first_digit + second_digit) # 45


# a = input("Enter the word: ")
# print(a[0:7:2])


# a = input("Enter the word: ")
# print(a[1:6:2])

#10.
# word = input("Enter the word: ") # Azerbaycan
#
# first_three = word[0:3] # Aze
# last_three = word[len(word)-3:] # word[7:] = can
#
# result = first_three + last_three
#
# print(result)
# first_three = word[0:3]
# last_element = word[-1]
#
# result = first_three + last_element
#
# print(result)

#11.
# a = input("Enter the number: ")
# print(a[len(a)//2])
