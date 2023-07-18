#syntax: range(start, stop, step)
#The range() function is used to generate a sequence of numbers over time.
#At its simplest, it accepts an integer and returns a range object (a type of Iterable)
#start:Optional. An integer number specifying at which position to start. Default is 0
#Stop:Required. An integer number specifying at which position to stop (not included).
#Step:Optional. An integer number specifying the incrementation. Default is 1
range_v = range(10)
print(type(range_v)) 
print(tuple(range_v)) #by default the range starts from 0 and 10 numbers will print from 0-9. the default incremental value is +1.

print(list(range(-100,-95))) #the nummbers will print between -95 and -100

v_range = range(3,10)
print('Range between the numbers are:' , list(v_range))
print('v_range datatype is:', type(v_range))

print(list(range(1,50,5))) #we have mentioned to increment the value by 5 from 1 till 50