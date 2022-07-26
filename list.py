list = ["chennai", "andra", "kerala"]
print(list)


list2 = ["chennai", "andra", "kerala", "andra", "kerala"]
print(list2)

list3 = ["chennai", "andra", "kerala"]
print(len(list3))


list4 = ["chennai", "andra", "kerala"]
print(type(list4))


# change

list5 = ["chennai", "andra", "kerala"]
list5[1] = "delhi"
print(list5)


# add

list6 = ["chennai", "andra", "kerala"]
list6.append("delhi")
print(list6)

# remove

list7 = ["chennai", "andra", "kerala"]
list7.remove("andra")
print(list7)

# copy

list7 = ["chennai", "andra", "kerala"]
list8 = list7.copy()
print(list8)


#sort

list9 = ["chennai", "andra", "kerala", "delhi"]
list9.sort()
print(list9)


# loop list

list9 = ["chennai", "andra", "kerala", "delhi"]
for x in list9:
  print(x)
print(mylist)
