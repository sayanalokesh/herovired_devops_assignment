#List is a collection which is ordered and changeable. Allows duplicate members. We represent in []

squares = [1,2,3,4,5]
print(squares) #[1, 2, 3, 4, 5]
print(type(squares)) #output <class 'list'>

mylist = ["Lokesh", "Mittu", "Dad", "Mom", "Pooji", 1 ,2,3,4,True, False] #if we enter any value in [], that means it is a list type
print(mylist)
print(type(mylist))

#lists can be indexed and sliced, we can specify the start and end point of the range

mylist = ["Orange", "apple", "banana", "kiwi", "papaya", "tomato", "pineapple"]
print(mylist[0:3]) # output ['Orange', 'apple', 'banana']
print(mylist[:7]) #output if we do not mention in the first place, it will start from index O['Orange', 'apple', 'banana', 'kiwi', 'papaya', 'tomato', 'pineapple']
print(mylist[2:]) #output ['banana', 'kiwi', 'papaya', 'tomato', 'pineapple']

mylist = "hello_world"
print(mylist[::-2])


