'''(1) wap to print 1 to 10'''
# for i in range(1, 11):
#     print(i)

'''(2) wap to print 10 to 1'''
# for i in range(10, 0, -1):
#     print(i)

'''(3) wap to print -1 to -10'''
# for i in range(-1, -11, -1):
#     print(i)

'''(4) wap to print -10 to -1'''
# for i in range(-10, 0):
#     print(i)

'''(5) wap to print even number 1 to 10'''
# for i in range(0, 10, 2 ):
#     print(i)

        #(or)

# for i in range(0, 11):
#     if i % 2 == 0:
#         print(i)

'''(5) wap to print odd number 1 to 10'''
# for i in range(1, 10, 2 ):
#     print(i)

          #(or)

# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)


'''(6) wap to  print travering through string '''
# string = 'python'
# for i in range(0, len(string)):
#     print(string[i])
#
#     (or)

# for char in string:
#     print(char, end=" ")

'''(7) wap to print traversing through list and tuple'''
# li = [1, 2, 3, 4, "python"]
# for i in range(0, len(li)):
#     print(li[i], end=" ")
# print()
#
# tup = (1, 2, 3+2j, "hai", "hello")
# for i in range(0, len(tup)):
#     print(tup[i], end=" ")
# print()
#
# set_ = {"python", "hello", "hai"}    ## check it
# for i in set_:
#     print(i, end=" ")


'''[DICTIONARY type ]'''

# d = {"one": 1, "two": 2, "three": 3}
# for i in d:
#     print(i, d[i], sep="-->")
# #
#     # (or)
#
# d = {"one": 1, "two": 2, "three": 3}
# for i in d:
#     print(i)
#
#     # (or)
#
# d = {"one": 1, "two": 2, "three": 3}
# for i in d:
#     print(i, d[i])



'''(8) wap to print index and element in a string'''
# string = "python"
# for i in range(0, len(string)):
#     print(i, string[i])

          #   (or)

'''using inbuilt function important (enumerate(iterable)) (q8)problem'''
# string = "python"
# for i in enumerate(string):
#     print(i)
#     print(i[0], i[1])

               #(or)

# string = "python"
# for index, item in enumerate(string):
#     print(index, "-->", item)





'''(9) wap to traverse to a string in reverse order'''
# string = "sharath"
# for i in range(len(string)-1, -1, -1):
#     print(string[i])

    #(or)

# string = "sharath"
# for i in string[::-1]:
#     print(i)


         #(or)

# string = "sharath"
# for i in reversed(string):
#     print(i)


'''(10) wap to count numberof character present in a string'''
# a = "python"
# count = 0
# for i in range(0, len(a)):
#     count+=1
# print(count)


'''(11) wap to print even index characters in a string'''
# a = "sharath"
# for i in range(0, len(a), 2):
#     print(a[i])
# print()

#            (or)

# for i in a[::2]:
#     print(i, end=" ")

#             (or)

# a="sharath"
# for i in range(0, len(a)):
#     if i%2==0:
#         print(a[i])


'''(12) wap to print the digit present inside the string'''
# s = "hello 123 %sharath%"
# for i in s:
#     if i.isdigit():
#         print(i)
# print()
#
# for i in s:
#     if "0" <= i <= "9":
#         print(i)


'''(13) wap to count the number of digits present inside the string'''
# s = "hello 123 %sharath%"
# count = 0
# for i in s:
#     if "0" <= i <= "9":    #if i.isdigit():
#         count+=1
# print(count)
# print()


