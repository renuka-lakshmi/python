"""
list is a collections/group of items/values/elements
they can be enclosed within the square brackets[] seperated by(,)
list methods: append/extend/count/mutability/index/remove/pop/insert
syntax:listname.methodname()

"""
#append: this method is used to add the elements
# list1=[ "india", "scotland", "spain"]
# print(list1)
# list1.append("london")
# print(list1)

# # extend:this method is used to add the elements at the end but
# # as a sublist

# list2=[ "guava", "orange", "apple", "kiwi"]
# print(list2)
# list2.extend( ["grapes", "dragon","pineapple", "blueberry"])
# print(list2)

#count: this method counts the number of repeated elements in a list
# flowers=[ "rose","sunflower", "jasmine", "mariegold", "lotus"]

# print(flowers.count("rose"))

#mutability----- changing the elements

# mylist4=["hello","ece",123,34.65,56+78j]
# print(mylist4)
# mylist4[2]="agri"
# print(mylist4) 


#pop---removes the elements using index

# mylist5=[12,34,565,78.9,34+56j,"hello"]
# print(mylist5)
# mylist5.pop(2)
# print(mylist5)
# #removes---removes the element directly
# mylist5.remove(34)
# print(mylist5)

#count--it counts the number of occurance
# of a item in a list

# mylist6=[22,33,33,22,55,22,44,67,22,22]
# print(mylist6.count(22))

#NOTE :IT WILL TAKE ATMOST ONLY ONE ARGUMENT

#INSERT--IT just inserts the elements into the list
#using the index

# mylist7=[22,33,44,55,66,77]
# print(mylist7)
# mylist7.insert(1,"hello")
# print(mylist7)
"note:in insert method no element is removed"
" they just replaces the position"

#index-- this method tells the 
# #index of first occurance when the element is repeated

# mylist8=[22,44,55,55,44,66,67,89]
# print(mylist8.index(44))#1
# print(mylist8.index(55))#2

# #reverse--it just reverse the elements in a list
# mylist8.reverse()
# print(mylist8)

# #COPY---IT JUST COPY THE ELEMENTS IN A LIST
# #one list to other
mylist9=[22,55,66,77,88.99]
print(mylist9)
mylist10=mylist9.copy()
print(mylist10)

#clear---it the elementsn in a sorting wAY
print(mylist10.clear())
print(mylist10)



#sort ---- it just arrange thne elements in a sorting way
mylist11=[22,23,34,56,78]
mylist11.sort()
print(mylist11)
mylist12=["a","d","f","r","t","u","p"]
mylist12.sort()
print(mylist12)
#mylist13=[12.123,"hello"]
#mylist13.sort()
#print(mylist13)

#IN 
