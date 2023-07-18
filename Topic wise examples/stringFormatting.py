#Python uses C-style string formatting to create new, formatted strings.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
#together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
#s –strings d –decimal integers (base-10) f –floating point display
#c –character b –binary o –octal x –hexadecimal with lowercase letters after 9
#X –hexadecimal with uppercase letters after 9 e –exponent notation

loc = "Hyderabad"
name = "Lokesh"

print('My name is %s and i am staying in %s' %(name, loc)) #instaed od using {} we are using %s to represent the string later we are assiging the varialbles of the string

x = 11
y = 12.550
print('This is an integer %d and and this is a float number is %f' %(x,y)) #we can pass on the values using %() sytax

print("{!s}".format("Lokesh")) #we can mention the value after {}.format()
print("{:s}".format("Sayana"))

print("{}, {}".format(1,12.5))
print("%d , %f"%(1.1,23))