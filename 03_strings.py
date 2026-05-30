course="Python's Course for Beginners"
print(course)
course='Python Course for "Beginners"'
print(course)
officer=''' 
Hi,Sunita

How are you?

Thank you
For your support




'''
print(officer)
course='Python Course for Beginners'
print(course[1])
print(course[-2])
print(course[0:4])
print(course[0:])
print(course[1:])
print(course[:5])
print(course[:])
course="Python for Beginners"
another=course[:]
print(another)
name='Jennifer'
print(name[1:-1])

#Formatted Strings
first = 'Yasmin'
last = 'Iqra'
message = first + ' [' + last + '] is a coder'
print(message)
message = first + 'last is a coder'
msg=f'{first} [{last}] is a coder'
print(msg)

#String Method
course='Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('h'))
print(course.find('F'))
print(course.find('Beginners'))
print(course.replace('Beginners' ,  'Absolute Beginners'))
print(course.replace('f' , 'G'))
print('python' in course)

