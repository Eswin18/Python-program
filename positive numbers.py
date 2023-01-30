#Poisitive numbers
list1 = [int(item) for item in input("Enter the list items : ").split()]
list2 = [int(item) for item in input("Enter the list items : ").split()]
pos_1=[num for num in list1 if num >=0]
pos_2=[num for num in list2 if num >=0]
print(pos_1)
print(pos_2)
