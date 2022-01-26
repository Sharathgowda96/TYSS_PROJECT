'''same question as if statement(refer conditional_statement_practice.py)'''


'''(1) [QUESTION IN conditional_statement_practice.py]'''
'''(1) WAPTC if the user input number is even or not'''
# number = 2
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd number")



'''(2) [QUESTION IN conditional_statement_practice.py]'''
'''(2) WAP to check if thw given character is in lower case or not'''

# char = "R"
# if ("a"<=char<="z"):
#     print(f"{char} is lowercase character")
# else:
#     if "A" <= char <= "Z":
#         print(f"{char} is uppercase character ")
#     else:
#         print(f"{char} is not an alphabet")

#                  (OR)

# char = "s"
# if ("a"<=char<="z"):
#     print(f"{char} is lowercase character")
# elif "A" <= char <= "Z":
#     print(f"{char} is uppercase character")

                # (OR)

#
# char = "shaRatH"
# if char.islower() == True:
#     print(f"{char} is lowercase character")
# else:
#     print(f"{char} is other then lowercase character")


#
'''(3) [QUESTION IN conditional_statement_practice.py]'''
'''(3) WAPTC IF THE GIVEN ELEMENT IS PRESENT IN COLLECTION OR NOT'''
# list = ["python", "java", "linux", "ruby", "nodejs"]
# element = "django"
# if element in list:
#     print(f"{element} is present in collection or list")
# else:
#     print(f"{element} is not present in collection or list")


'''(4) WAPTC IF THE GIVEN ITERABLE IS EMPTY OR NOT'''
# iterable = "hai"
# if len(iterable) > 0:
#     print("the iterable is not empty")
# else:
#     print("iterable is empty")

    #       (OR)

# if bool(iterable):
#     print("iterable is not empty")
# else:
#     print("iterable is empty")

#         (OR) #USE THIS METHOD

# if iterable:
#     print("not empty")
# else:
#     print("empty")


'''(5) WAPTC the given value is default or non default value'''
# value=[]
# if value:
#     print("it is non default value")
# else:
#     print("default value")


'''(6) wapt convert lower case to uppercase and upper case to lower'''
# value="haiHELLO"
# if "a"<=value<="z":
#     upper_char = value.upper()
#     print(upper_char)
# elif "A"<=value<="Z":
#     lower_char = value.lower()
#     print(loer_char)
# else:
#     print("character is not an alphabet")

                      # (OR)

# value = "sharath"
# if value.islower():
#     print(value.upper())
# elif value.isupper():
#     print(value.lower())
# else:
#     print("character is not an alphabet")


                    # (OR)


# char = "n"
# if "a" <= char <= "z":
#     print(chr(ord(char)-32))
# elif "A" <= char <= "Z":
#     print(chr(ord(char)+32))
# else:
#     print("character is not a present")


'''(7) WAPT CHECK IFTHE STRING IS STARTING WITH VOWEL OR NOT'''

# char = "Apple"
# if char[0] in 'AEIOUaeiou':
#     print("vowel is present at 1st char")
# else:
#     print("vowel is not present 1st char")


'''(8) WAPTC if the given string is ending with vowel or not'''
# char = "Apple"
# if char[-1] in 'AEIOUaeiou':
#     print("end character is in vowel")
# else:
#     print("end character is not a vowel")



'''(9) check if the string is palendrom or not'''

# char = "malayalam"
# a = char.lower()
# if char == char[::-1]:
#     print(f"{char} is palendrom")
# else:
#     print(f"{char} is not palendrom")

'''(10) WAPTC if the integer is palendrom or not'''
# char = 121
# if str(char) == str(char)[::-1]:
#     print(f"{char} is palendrom")
# else:
#     print(f"{char} is not a palendrom")

             # (OR)

# char = 121
# str_num = str(char)
# if str_num == str_num[::-1]:
#     print(f"{char} is palendrom")
# else:
#     print(f"{char} is not a palendrom")


'''(11) WAP to check if the iterable has even number of elements or not'''

# char_ = [1, "hai", 2, 3, "hello", 4, "python", 3+2j]
# if len(char_) % 2 == 0:
#     print("even number of element")
# else:
#     print("not a even number of element")



'''(12) WAPTC if the first digit in the given number is even or odd '''
# char_ = 125
# if int(str(char_)[0]) % 2 == 0:  # (first need to doindex to take first character using str.
#                                   # later to % need to be in integer datatype)
#     print("even first digit")
# else:
#     print("odd first digit")


''' (ASSIGNMENT Q1) greatest among 3 number'''
# a = 10
# b = 20
# c = 15
# list = [a, b, c]
# max_num = max(list)
# print(max(list))   #inbuilt fnction

''' (ASSIGNMENT Q2) vowel value store to dict'''
# char = "a"
# d={}
# if char.lower() in "aeiou":
#     d[char] = ord(char)
# print(d)

             #(OR)

# char = "a"
# d={}
# if char.lower() in "aeiou":
#     d.update({char: ord(char)})
# print(d)

          #(OR)

# char = "a"
# d={}
# if char.lower() in "aeiou":
#     d.setdefault(char, ord(char))
# print(d)

       #(OR)

# char = "a"
# d={}
# if char.lower() in "aeiou":
#     print({char: ord(char)})
# print(d)
