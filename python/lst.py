#lst = [] --- single variable to store multiple values
##lst ordered , mutable ,
#  allow duplicate values and heterogeneous
##list is indexed

# lst = [1,2,"hello",True,1.2]
# print(lst)
# print(type(lst))

##indexing and slicing 
##indexing -- single character access 
##slicing -- multiple character access

# print(lst[0:2])
##access the item and the update it 
# lst[0] = "green"
##slicing 
# lst[0:1] = ["green","a","b"]
#methods of list
# print(lst.count("red"))
# print(lst.index("red"))
# lst.clear()
# del lst
# lst2 = lst.copy()
# lst.append("green")
# lst.extend(["green","a","b"])
# lst.insert(0,"green")
lst = ['red',"black","blue","red"]
# lst.pop(1)
# lst.remove("red")
# lst.reverse()
lst.sort(reverse=True)
print(lst)  #clear vs del 
# print(lst)
