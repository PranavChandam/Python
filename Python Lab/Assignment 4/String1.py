str="Hello World!!!!"

str = "Hello Word!!!"

print(str.lower())  

print(str.upper())  

print(str.capitalize()) 

print(str.title()) 

print(str.swapcase())  

print(str.strip())  

print(str.replace("Word", "World"))  

print(str.split(" "))  

print(str.find("Word")) 

print(str.startswith("Hello")) 

print(str.endswith("!!!"))  

print(str.isalpha())  

print(str.isdigit())  

print(str.count("l"))  

print(str.index("Word")) 

print(" ".join(["Hello", "World"]))  

print(str.zfill(15))  


print("Length of String: ", len(str))
print("String is Alphabets: ", str.isalpha())
print("String is Alphabets: ", str.isalnum())
print("String is Alphabets: ", str.islower())
print("String is Alphabets: ", str.isupper())
print("String is Alphabets: ", str.isspace())

print("String is Alphabets: ", str.istitle())



print(str.rfind("o"))  
print(str.rindex("o"))  
print("Hello\nWorld".splitlines())
print("Hello\tWorld".expandtabs(4)) 
print(str.ljust(20, '*'))  
print(str.rjust(20, '*'))  
print(str.center(20, '*'))  
print(str.partition("Word"))  
print(str.rpartition("o"))  
print(str.rstrip("!"))  
print(str.lstrip("H"))  
print(str.islower())  
print(str.isupper())  
print(str.istitle())  
print(str.isspace())  
print("Hello {}!".format("World"))  
print(str.removeprefix("Hello "))  
print(str.removesuffix("!!!")) 

