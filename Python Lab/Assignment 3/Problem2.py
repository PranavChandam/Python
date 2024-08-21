#check if a list contains palindrome of elements
list=[1,2,3,2,1]
L=list.copy()
L.reverse()
if L==list:
    print("List is palindrome")
else:
    print("List is not palindrome")