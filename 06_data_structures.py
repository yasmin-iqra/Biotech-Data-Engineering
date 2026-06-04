# 1.Tupels
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
numbers=(1,2,3)
print(numbers[0])

# 2.Unpacking
#---------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
coordinates=(1,2,3)
x,y,z=coordinates
print(x)
print(y)

# 3. Dictionaries
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
customer={
    "name":"Yasmin Iqra",
    "age":30,
    "is_varified":True
}
customer["name"]="Iqra Yasmin"
print(customer["name"])
print(customer.get("birthday"))
print(customer.get("birthdate","Feb 21 2004"))
#Exercise= digit to word
phone=input("Phone:")
digit_mapping={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output=""
for ch in phone:
   output += digit_mapping.get(ch,"!") +""
   print(output)

# 4.Emoji Converter
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
message=input(">")
words=message.split(' ')
emojis={
   ":)":"😊",
   ":(":"🥹"
}
output=""
for word in words:
  output += emojis.get(word,word)  + " "
  print(output)

# 5.Functions
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def greet_user():
   print('Hi there!')
   print('Welcome aboard')


print("Start")
greet_user()
print("Finish")

# 6.Parameters
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
def greet_user(first_name,last_name):
   print(f'Hi {first_name} {last_name}!')
   print('Welcome aboard')


print("Start")
greet_user('Iqra', 'Yasmin')
print("Finish")

# 7.Keywords Arguments
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
def greet_user(first_name,last_name):
   print(f'Hi {first_name} {last_name}!')
   print('Welcome aboard')


print("Start")
greet_user(last_name='Iqra', first_name='Yasmin')
print("Finish")


def greet_user(first_name,last_name):
   print(f'Hi {first_name} {last_name}!')
   print('Welcome aboard')


print("Start")
greet_user('Iqra', first_name='Yasmin')
print("Finish")


  


