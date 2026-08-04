#print functions
#built-in function to print output to the console
print("hello world!")
print('hello world!')

#data types
#string data type using single,double and triple quotes(multi-line string)
variable1 = "Amna"
variable11 = """ hello my name is amna and I am learning python i am from the holand pakistan
I am learning python from the start and I am enjoying it"""
#integer data type
variable2 = 10
#boolean data type
variable3 = True
#float data type
variable4 = 10.5
#printing the variables
print(variable11)
print(variable1)
print(variable2)
print(variable3)
print(variable4)
#data type printing
print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))
#operators
print(10+5)
print(10-5)
print("hi*5")
print("hi"*5)

variable1=variable1.lower()
print(variable1)
variable1=variable1.upper()
print(variable1)
variable1=variable1.capitalize()
print(variable1)
variable1=variable1.replace("Amna","Amna Khan")
print(variable1)

#list can hold multiple data types mutable data type and ordered data type
list1=["Amna","pakistan","holand"]
print(list1)
print(type(list1))
print(list1[0])
print(list1[-1])
print(list1[1])
print(list1[1:3])
list2=["amna",7,"nature",True,10.5]
print(list2)
#dictionary can hold multiple data types but it is unordered and mutable data type
dic={
    "name":"Amna",
    "country":"Pakistan",
    "number":7,
    "email":"mdnc@gcb.pk"
}
dic["name"]="Amna Khan"
print(dic)
print(type(dic))
print(dic["name"])
print(dic.keys())
print(dic.values())
print(dic.items())

#sets unchangable and unordered data type can add or remove but cannot change the existing values
set1={"Amna","pakistan","holand"}
print(set1)
set1.add("nature")
set1.remove("pakistan")
print(set1)
print(type(set1))
print(sorted(set1))

#tuple can hold multiple data types but it is ordered and immutable data type
tuple1=("Amna","pakistan","holand")
print(tuple1)
#operators
print(2==3)
print(2!=4)
print(2>6)
print(0<7)
print(9>=9)
#logical operators
print(2==2 and 3==3)
print(2==2 or 3==4)
print(not(2==2))

#conditional statements
if 2==2:
    print("2 is equal to 2")

pasta_quantity=5400
pasta_quality=3000
if pasta_quantity>pasta_quality:
    print("pasta is avaliable")

elif pasta_quantity<5000 :
    print("nearly enough pasta is avaliable")
 
else:
    print("pasta is not avaliable")

if 2==2:
    print("2 is equal to 2")
else:
    print("2 is not equal to 2")

#loops 
#for loop
ingredients=["pasta","tomato","onion","garlic"]
for i in ingredients:
    print(i) 

quanities=[5400]
for i in quanities:
  if i>2000:
     print("enough quantity is avaliable")
  elif i<2000:
     print("not enough quantity is avaliable")

  else:
        print("quantity is not avaliable")
ppt={
    "name":"Amna",
    "country":"Pakistan",
    "number":7,
    "email":"nanns@ncb.com"
}
for key,value in ppt.items():
    print(key,value)
#while loop
i=5
while i<5:
    print(i)
#task from day 1
#sum average max min USING  LOOPS
task=[12, 45, 7, 23, 9]
total=0
maximum=task[0]
minimum=task[0]
for i in task:
    total+=i
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print("maximum:", maximum)
print("minimum:", minimum)
average=total/len(task)

print("Sum:", total)
print("Average:", average)

# total=sum(task)
# average=total/len(task)
# maximum=max(task)
# minimum=min(task)
# print("Sum:", total)
# print("Average:", average)
# print("Maximum:", maximum)
# print("Minimum:", minimum)
#sum average max min USING  LOOPS