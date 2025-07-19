my_list = [1.0,2.0,3.0]
type(my_list)
print(type(my_list))
#-------------------------
# this will repeat the list elements twice
print(my_list*2)
#-------------------------
# lists can have elements of different data types
my_list2 = ["hello", 12, 1.5, 'hi']
print(my_list2)
print(len(my_list2))
print(type(my_list2))
#-------------------------
#concatination
my_list2 = my_list2 + [3]
print(my_list2)
my_list2 = my_list2 + ['good']
print(my_list2)
#-------------------------
my_list2 =["first"] + my_list2
print(my_list2)

#-------------------------
# usefull functions

#indexing and slicing
my_list3 =["hi", 12, "good","hello"]
print(my_list3[2][-1])
#-------------------------
#slicing
new_list =my_list3[:2]
print(new_list)
#-------------------------
# append
my_list2.append(1000)
print(my_list2)
#-------------------------
# insert
my_list2.insert(1,"insert")
print(my_list2)
#-------------------------
# extend
my_list3.extend(my_list)
print(my_list3)
#-------------------------
#remove
my_list3.remove("good")
print(my_list3)
#-------------------------
# pop  if you pass a position it will remove the item in the position or it will remove the last item
my_list3.pop(2)
print(my_list3)
my_list3.pop()
print(my_list3)
#-------------------------
#clear remove all items from the list without removing the list
my_list3.clear()
print(my_list3)

#-------------------------