# lambda function followed by one or more argumants ,a colon and an expresion
print((lambda x:sum(x)/len(x))([3,6,9]))
# store lambda function as varialbe
average =(lambda x:sum(x)/len(x))
print(average([3,8,10]))

# with multiple atrguments
mul=(lambda x,y:x**y)
print(mul(2,3))

""" lambda function with iterable
map() applies a function to all elements in iterable
"""
names=["ali","shah","ayat","hoor"]
capitalize=map(lambda x:x.capitalize(),names)
print(capitalize) 
print(list(capitalize))
print(type(capitalize))
# error : type-error,value-error,
