
''' WAPTC IF THE GIVEN ITERABLE IS EMPTY OR NOT'''
iterable = "hai"
if len(iterable) > 0:
    print("the iterable is not empty")
else:
    print("iterable is empty")

             (OR)

if bool(iterable):
    print("iterable is not empty")
else:
    print("iterable is empty")