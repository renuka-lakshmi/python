"""
tuple is a collection of elements/items/values
they are enclosed within parenthesis or
open brackets() seperated by (,)
as atuple are imutable it mean we cant change
so when the data is fixed we can go with tuples

"""

#eg.1
mytuple=(13,12,11)
print(type(mytuple))#<class tuple>
mytuple2=()#empty tuple
print(type(mytuple2))#<class tuple>
mytuple3=(10)
print(type(mytuple3))#<class int>

"""
NOTE: WHEN YOU WANA CREATE A TUPLE WITH SINGLE VALUE
IT SHOULD BE SEPERATED BY SO THAT THE COMPILER  
TREATS AS TUPLE OR ELSE IT JUSTS TREATS AS INTEGER

"""
#CREATION OF TUPLE
#syntax:tuplevariable=(val1,val2,val3,......valn)
mytuple5=(12,23.45,45+56j,[12,34,45],"hello",(123,"ece"))
print(mytuple5)

#creating the tuple with asingle element
mytuple6=(45,)
print(type(mytuple6))

#creating the tuple with a list
t=[23,45,56,"kk"]
print(t)
k=tuple(t)
print(k)

#CREATING THE TYUPLE WITH TUPLE "TUPLE" PREDEFINED WORD
t=tuple()#it consider as empty tuple
print(t)





