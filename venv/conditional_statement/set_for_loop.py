'''(1) wap to traverse through set and print each element'''
# set_ = {"python", "dad", "hai", "malayalam", "madam", "mom"}
# for i in set_:
#     print(i)
#
'''(2) wap to print the elements in the set in reversed order'''
# we cannot reverse the set by slicing and reversed inbuilt function


'''(3) wap to remove the given element from the set'''
# set_ = {"python", "dad", "hai", "malayalam", "madam", "mom"}
# n = "hai"
# for i in set_:
#     if i == n:
#         set_.discard(n)
#         break
# print(set_)
# print()

''' same as above question if we not use break means afer the first round of exicution the set will shafal because 
   it is unorder way shafal it so without break it will not exicute'''

''' without break we can do like this directly'''
# set_.discard(n)
# print(set_)


'''(4) wap to create a set with the element in list if the element is palindrome'''
# set_ = ["python", "dad", "hai", "malayalam", "madam", "mom"]
# res = set()
# for i in set_:
#     if i == i[::-1]:
#         res.add(i)             #res.update([i])
# print(res)
