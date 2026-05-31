# Arithmetic Operations
#--------------------------------------------
#--------------------------------------------
print(10*7)
print(20-13)
print(30+5)
print(40/10)
print(40//4)
print(10%2)
print(10**4)
x=20
x=x+20
print(x)
y=10
x=y+4
print(x)
# Augmented Assignment Operator
x=10
x += 3
x -=3
print(x)
# ------------------------------------------------------------
#-------------------------------------------------------------
# 2.Operator  Precedence
x=10+3*2
print(x)
# Exponentiation 2 ** 3
# Multiplication or Division
# Addition or Subtraction
x=10+3*2**2
print(x)
x = (10+3) * 2 ** 2
print(x)
x = (2+3) * 7-3
print(x)
#----------------------------------------------------------------
#-----------------------------------------------------------------
# Math Functions
x=2.9
print(round(x))
x=2.9
print(abs(-2.9))
import math
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.acosh(2.9))
#----------------------------------------------------------------
#----------------------------------------------------------------
# If Statements
# exercise: if its hot its a hot day,drink plenty of water,otherwise if its cold,wear warm clothes,otherwise its a lovely day
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")
print("Enjoy your day")
#Exercise :price of a house is $1M,if buyers has good credit,they nedd to put down 10%,otherwise they need to put down 20%
price=1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment:${down_payment}")

 #--------------------------------------------------------------------------------
 #--------------------------------------------------------------------------------
 # Logical Operator
 # Exercise : If applicant has high income and good credit then he will eligible for loan
has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
    print("Eligible for loan")
# exercise: if applicant has high income or good credit then he will eligible for loan
has_high_income=False
has_good_credit=True
if has_high_income or has_good_credit:
    print("Eligible for loan")
#if applicant has good credit and doesn't have a criminal record then he will eligilbe for loan
has_good_credit=True
has_criminal_record=False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
# Comparison Operators
# Exercise: If temperature is greater than 30 its a hot day,otherwise if its less than 10 iys a cold day, otherwise its neither hot nor cold
temperature=30
if temperature>30:
    print("It's a hot day")
else:
    print("it's not a hot day")
# exercise : if name is less than 3 characters long name must be at least 3 characters,otherwise if its more than 50 characters long name can be maximum of 50 charaters,otherwise names looks good
name="J" 

if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Na e must be a maximum of 50 characters")
else:
    print("Name looks good")
    




