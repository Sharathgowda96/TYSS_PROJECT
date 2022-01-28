'''(1) Traversing throuugh 3 iterables simultaneously'''

# s1 = "hai"
# s2 = "hey"
# s3 = "are"
# # print(zip(s1, s2)                #  pending problem
#
# for i1, i2,
#



'''(2) different lengths'''
# s = "hai"
# s1 = "hello"
# for i1, i2 in zip(s, s1):
#     print(i1, i2)
# print()
#
#
# from itertools import zip_longest
# for i1, i2 in zip_longest(s, s1, fillvalue="not present"):
#     print(i1, i2)
# zip()



#
# for num in range(-2,-5,-1):
#     print (num, end" ")


'''(3) wap to print key in a dictionary'''
# a = {"a":1, "b":2, "c":3, "d":4, "e":5}
#
# # normal method traversing through dictionary directly
# for key in a:
#      print(key, end=" ")
# print()
#
#
# # a.keys
# for key in a.keys():
#     print(key, end=" ")
# print()
#
#
# # a.items()
# for key, value in a.items():
#     print(key, end=" ")



'''(4) wap to print only the values from the dictionary'''
# a = {"a":1, "b":2, "c":3, "d":4, "e":5}
# # using a.items
# for key, value in a.items():
#     print(value, end=" ")
# print()
#
# # using dictionary keys
# for key in a:
#     print(a[key], end=" ")
# print()
#
# # using get() method
# for key in a:
#     print(a.get(key), end=" ")
# print()
#
# # using a.values()
# for value in a.values():
#     print(value, end=" ")

'''(5) wap to print the items in a dictionary along with their indices'''
# d = {"a":1, "b":2, "c":3, "d":4, "e":5}
#
# # applying enumerate on dictionary variable
# for item in enumerate(d):
#     print(item, end=" ")
# print()
#
# # enumerate(d.items())
# for index, (key, value) in enumerate(d.items()):
#     print(index, key, value, end=" ", sep="-")


'''(6) wap tp create a dictionary with word and its count pair in a string'''
# string = "hello world"
#
# # count()
# d = {}
# for char in string:
#     d[char] = string.count(char)
# print(d)
# print()

# # using set() this is correct method using inbult
# string = "hello world"
# d = {}
# for char in set(string):
#     d[char] = string.count(char)
# print(d)

# normal method
# string = "hello world"
# d = {}
# for i in set(string):
#     c = 0
#     for j in string:
#         if i == j:
#             c+=1
#     d[i] = c
# print(d)
# print()

# one more normal method
# string = "hello world"
# d = {}
# for char in string:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# print(d)
# print()

# one more normal method
# string = "hello world"
# d = {}
# for char in string:
#     d[char] += 1
# print(d)

'''NOTE :- refer notes'''
# from collections import defaultdict
# s = "hello world"
# dd = defaultdict(int)
# print(dd)
#
# for char in s:
#     dd[char] = dd[char] + 1
# print(dd)



''' (7) wap to create a dictionary with word and count pair'''

#normal method
# string = "python is a language, python programming is eassy"
# d = {}
# d1 = string.split()
# for char in set(d1):
#     d[char] = d1.count(char)
# print(d)
# print()


# without using inbuilt function
# string = "python is a language, python programming is eassy"
# d = {}
# list_ = string.split()
# for char in list_:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# print(d)
# print()
#
#
#
# from collections import defaultdict
# string = "python is a language, python programming is eassy"
# dd = defaultdict(int)
# print(dd)
#
# for char in string.split():
#     dd[char] = dd[char] + 1
# print(dd)
# print()


'''(8) wap to create a dictionary with word and its length pair'''
# string = "python is a language, python programming is eassy"
# d = {}
# d1 = string.split()
# for i in d1:
#     d[i] = len(i)
# print(d)

''' (9) wap to create a dictionary with word and its length pair only if the word is of even length'''
# string = "python is a language, python programming is easy"
# d = {}
# d1 = string.split()
# for i in d1:
#     if len(i) % 2 == 0:
#         d[i] = len(i)
# print(d)

''' (10) wap to createa dictionary with word and its length pair only if the word is starting with vowel'''
# s = "apple is good for a health"
# d = {}
# d1 = s.split()
# for i in d1:
#     if i[0].lower() in "aeiou":
#         d[i] = len(i)
# print(d)


'''(11) wap to create a dictionary with word and its count only if the word is not repeadted'''
# s = "python is a language, python programming is easy"
# d = {}
# d1 = s.split()
# for i in d1:
#     if d1.count(i) == 1:
#         d[i] = d1.count(i)
# print(d)
# print()

# one more method
# s = "python is a language, python programming is easy"
# d = {}
# d1 = s.split()
# for i in d1:
#     if not d1.count(i) == 1:
#         continue
#     else:
#          d[i] = d1.count(i)
# print(d)


''' (12) wap to reverse the values in the dictionary if the value is of type string '''
# d = {"a": "hello", "b": 100, "c": 10.2, "d": "world"}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
# print(d)


''' (13) wap to get all duplicated items and the number of item repeated in the list'''
# d = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# res = {}
# for name in d:
#     count = d.count(name)
#     if count > 1:
#         res[name] = count
# print(res)


"""(14) wap to get the following output"""
''' sentence = "hello world welcome to python programming hi there" '''
''' output = {"h":["hello","hi"], "w":["world","welcome"], "t":["to","there"], "p":["python","programming"]}  '''

# sentence = "hello world welcome to python programming hi there"
# list_ = sentence.split()
# d = {}
# for word in list_:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]] +=[word]      # / d[word[o]].append(word)
# print(d)
# print()



# from collections import defaultdict
# sentence = "hello world welcome to python programming hi there"
# dd = defaultdict(list)
# list_ = sentence.split()
# for word in list_:
#     dd[word[0]] += [word]
#     #dd[word[0]].append(word)
# print(dd)


''' (15) wap to create a dictionary with element and its index pair in the given list'''

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# d = {}
# for index, key in enumerate(names):
#     if key not in d:
#         d[key] = [index]
#     else:
#         d[key].append(index)
# print(d)
# print()



# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
#
# from collections import defaultdict
# dd = defaultdict(list)
#
# for index, key in enumerate(names):
#     dd[key] += [index]
# print(dd)



''' wap to flip key and value in a dictionary'''

# d = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# d1 = {}
# for key, value in d.items():
#     d1[value] = key
# print(d1)


# d = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# d1 = {}
# for key in d:
#     value = d[key]
#     d1[value] = key
# print(d1)

