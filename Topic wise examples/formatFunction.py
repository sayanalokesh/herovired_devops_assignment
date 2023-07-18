name = "Lokesh"
age = 29
sal = 100000
bonus = 5000
tot_sal = sal+bonus
print("my name is {}, my age is {}, my sal is {}".format(name, age, tot_sal)) #The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
print('my name is {name}, I stay in {Loc}, my sal is {tot_sal}'.format(name='Lokesh', Loc = 'Hyderabad', tot_sal = 'tot_sal')) #we can also pass the values in the format() and the empty places will occupy based on the left and right position
print('my name is {2}, I stay in {1}, my sal is {0}'.format(105000, "Hyderabad", "Lokesh")) #we can also use {}.format() by using index places
