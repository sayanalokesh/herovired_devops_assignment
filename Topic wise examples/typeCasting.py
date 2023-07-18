x = int(2) #we are mentioning a number inside an intiger
y = int(2.8) #we gave a float value however we have mentioned inside an int therefore it became an int
z = int("3") #we have entered a string value however we have mentioned inside an int, hence it became int value
a = "45" #we have entered a string value
b = 2
c = int(a)+b
print(type(x),type(y),type(z)) #output <class 'int'> <class 'int'> <class 'int'>
print(f'type of c is {type(c)} and value of c is {c}') #Output 47 because we have typecasted a from string to integer

a = str("45")
b = str("22")
print(f' the type of a and b is {type(a),type(b)} and the values of a and b are {a,b}') #output the type of a and b is (<class 'str'>, <class 'str'>) and the values of a and b are ('45', '22')

# print(type(x,y,z)) #we should mention only one argument inside type(), we can't mention all the variables inside type()