# i=0
# while i<=50:
#   print("pass",i)
#   i+=1

# # h.w 
# # 1. 

# i=50
# while i>=0:
#   print("pass",i)
#   i-=1

# # h.w 
# # 2. 
# i=int(input("enter num: "))
# j=1
# while j<=10:
#   print(i,"*",j,"=",i*j)
#   j+=1

# # h.w 
# # 3. 
# range={1:2,2:4,34:5,4:0}
# for item in range:
#  print(item)
#  print(range[item])
# print(type(range))

# # h.w 
# # 4. 

# list=[]
# i=1
# while i<=10:
#     m=i**2
#     list.append(m)
#     i+=1

# print(list)

# # h.w 
# # 5.

# tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 

# print(type(tuple)) 

# i=0
# while i<len(tuple):
#     print(tuple[i])
#     i+=1

# h.w 6
# i=1
# while i<=10:
#   print("pass",i)
#   if(i==5):
#       break
#   i+=1

# h.w 7

# i=1
# while i<=10:
#   if(i%2!=0):
#       i+=1
#       continue
#   print(i)
#   i+=1
  
# h.w 8
  
# i=1
# while i<=10:
#   if(i%2!=0):
#       i+=1
#       continue
#   print(i)
#   i+=1
  
  
# for loop
# range=[11,22,33,44]
# tup=[1,2,3,4]
# for item in range:
#  print(item)
# for item in tup:
#  print(item)
 
# for item in (1,3,5):
#  print(item)

# # Factorial of 5 is 120

# number = 5
# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print("Factorial of", number, "is", factorial)



# Define a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Iterate over the dictionary
for key, value in person.items():
    print(key + ":", value)
