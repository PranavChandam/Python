
my_list = [3, 1, 4, 1, 5, 9]


my_list.append(2)
print("After append(2):", my_list)


my_list.extend([6, 5, 3])
print("After extend([6, 5, 3]):", my_list) 


my_list.insert(2, 10)  
print("After insert(2, 10):", my_list)  


my_list.remove(1)  
print("After remove(1):", my_list)  


popped_element = my_list.pop(3)  
print("After pop(3):", my_list) 
print("Popped element:", popped_element) 


my_list.clear()
print("After clear():", my_list)  

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


index_of_5 = my_list.index(5)
print("Index of first occurrence of 5:", index_of_5) 


count_of_1 = my_list.count(1)
print("Count of 1:", count_of_1)  

my_list.sort()
print("After sort():", my_list)  


my_list.reverse()
print("After reverse():", my_list)  
