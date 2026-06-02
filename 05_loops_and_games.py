# 1.Weight Converter
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
weight=int(input('weight:'))
unit=input('(L)bs or (K)g:')
if unit.upper()=="L":
    converted=weight*0.45
    print(f"You are {converted}kilos")
else:
    converted=weight/0.45
    print(f"You are {converted}pounds")

# 2.While Loops
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
guess_count=1
while guess_count <= 5:
    print(guess_count)
    guess_count=guess_count+1
print("Done")
guess_count=1
while guess_count <= 5:
    print('*'* guess_count)
    guess_count=guess_count+1
print("Done")

# 3. Guessing Game
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
secret_number = 9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
   guess=int(input('Guess: '))
   guess_count+=1
   if guess == secret_number:
     print('You won!')
     break
else:
    print("Sorry,you failed!")

# 4.Car Game
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
command=""
started=False
while True:
    command=input(">").lower()
    if command =="start":
       if started:
        print("Hey,car is already started!")
       else:
        started=True
        print("Car started...")
    elif command =="stop":
        if not started:
           print("Car is already stopped!")
        else:
           started=False
        print("Car stopped.")
    elif command =="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
              """)
    elif command == "quit":
        break
    else:
        print("Sorry,I don't understand that!")

# 5.For Loops
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
for item in "Python":
   print(item)
for item in ['Iqra','Manha','Yasmin']:
   print(item)
for item in range(5,10,2):
    print(item)
for item in range(10):
   print(item)
for item in range(5,10):
   print(item)
#Exercise:list of prices
prices=[10,20,30]
total=0
for price in prices:
   total+=price
print(f"Total: {total}")

# 6.Nested Loops
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
for x in range(4):
   for y in range(3):
      print(f'({x},{y})')
# Exercise :Making F with X
numbers=[5,2,5,2,2]
for x_count in numbers:
   print('x'*x_count)
# Using nested loop
numbers=[5,2,5,2,2]
for x_count in numbers:
   output=''
   for count in range(x_count):
      output+='x'
      print(output)

# 7.Lists
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
names=['Iqra','Bob','Sarah','Manha']
names[0]='piku'
print(names[-1])
print(names[3])
print(names[2:])
print(names[2:4])
print(names[:])
# Exercise: Write a program to find the largest number in a list
numbers=[2,4,32,6,88,87]
max=numbers[0]
for number in numbers:
   if number>max:
      max=number
      print(max)

# 8.2D Lists
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
matrix=[
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
matrix[0] [1]=20
print(matrix[0][1])
matrix=[
   [3,4,5],
   [1,4,7],
   [1,5,2]
]
for row in matrix:
   for item in row:
      print(item)

# 9.List Methods
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
numbers=[2,4,1,7,8,5]
numbers.append(11)
print(numbers)
numbers=[2,4,5,7,23]
numbers.insert(0,10)
print(numbers)
numbers=[1,2,3,4,2]
print(numbers.index(4))
print(50 in numbers)
print(numbers.count(2))
print(numbers.sort())
numbers=[2,3,1,5,7,9,3]
numbers.sort()
numbers.reverse()
print(numbers)
numbers=[1,2,3,6,4,6]
numbers2=numbers.copy()
numbers.append(10)
print(numbers2)
#Exercise:Write a program to remove the duplicates in a list
numbers=[2,3,2,4,5,4,6,7,8,,6]
uniques=[]
for number in numbers:
   if number not in uniques:
      uniques.append(number)
      print(uniques)
      




                    